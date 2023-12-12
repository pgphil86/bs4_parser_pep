import logging
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests_cache
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import BASE_DIR, EXPECTED_STATUS, MAIN_DOC_URL, PEP_DOC_URL
from outputs import control_output
from utils import find_tag, get_response


def whats_new(session):
    """
    Python version list display function.
    """

    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')

    response = get_response(session, whats_new_url)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features='lxml')
    main_div = find_tag(soup, 'section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = find_tag(main_div, 'div', attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all(
        'li',
        attrs={'class': 'toctree-l1'}
    )

    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]

    for section in tqdm(sections_by_python):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(whats_new_url, href)
        response = get_response(session, version_link)
        if response is None:
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        h1 = find_tag(soup, 'h1')
        dl = find_tag(soup, 'dl')
        dl_text = dl.text.replace('\n', ' ')
        results.append(
            (version_link, h1.text, dl_text)
        )

    return results


def latest_versions(session):
    """
    A parser that collects information about Python versions.
    """

    response = get_response(session, MAIN_DOC_URL)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features='lxml')
    sidebar = find_tag(soup, 'div', {'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')
    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise Exception('Ничего не нашлось')

    results = [('Ссылка на документацию', 'Версия', 'Статус')]

    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for a_tag in a_tags:
        link = a_tag['href']
        text_match = re.search(pattern, a_tag.text)
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append(
            (link, version, status)
        )
    return results


def download(session):
    """
    A parser that downloads an archive with Python documentation.
    """

    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')

    response = get_response(session, downloads_url)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features='lxml')
    table_tag = find_tag(soup, 'table', {'class': 'docutils'})
    a4_tag = find_tag(table_tag, 'a',
                      {'href': re.compile(r'.+pdf-a4\.zip$')}
                      )
    a4_link = a4_tag['href']
    archive_url = urljoin(downloads_url, a4_link)
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    response = session.get(archive_url)
    with open(archive_path, 'wb') as file:
        file.write(response.content)
    logging.info(f'Архив был загружен и сохранён: {archive_path}')


def pep(session):
    """
    A parser of data about PEP documents.
    """

    response = get_response(session, PEP_DOC_URL)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features='lxml')
    section_tag = find_tag(soup, 'section', attrs={'id': 'numerical-index'})
    tbody_tags = find_tag(section_tag, 'tbody')
    tr_tag = tbody_tags.find_all('tr')
    results = [('Статус', 'Количество')]
    total = 0
    status_count = {}
    for tr_tag in tqdm(tr_tag):
        preview_status = find_tag(tr_tag, 'abbr').text[1:]
        pep_a_tag = find_tag(tr_tag, 'a')
        pep_link = urljoin(PEP_DOC_URL, pep_a_tag['href'])
        response = get_response(session, pep_link)
        if response is None:
            return
        soup = BeautifulSoup(response.text, features='lxml')
        section_tag = find_tag(soup, 'section', attrs={'id': 'pep-content'})
        dl_tag = find_tag(
            section_tag,
            'dl',
            attrs={'class': 'rfc2822 field-list simple'}
        )
        dl_string = dl_tag.find(string='Status')
        pep_status_page = dl_string.parent.find_next_sibling('dd').string
        status_count[pep_status_page] = status_count.get(pep_status_page,
                                                         0) + 1
        try:
            if pep_status_page not in EXPECTED_STATUS[preview_status]:
                logging.info(
                    f'Несовпадающие статусы:\n'
                    f'{pep_link}\n'
                    f'Статус в карточке: {pep_status_page}\n'
                    f'Ожидаемые статусы: {EXPECTED_STATUS[preview_status]}\n'
                )
        except KeyError:
            logging.error(f'Ошибка кода статуса {preview_status}')
        total += 1
    results.extend(status_count.items())
    results.append(('Total', total))
    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep,
}


def main():
    configure_logging()
    logging.info('Парсер запущен!')

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')

    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()
    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)
    if results is not None:
        control_output(results, args)
    logging.info('Парсер завершил работу.')


if __name__ == '__main__':
    main()
