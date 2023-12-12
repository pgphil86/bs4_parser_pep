import logging

from requests import RequestException

from exceptions import ParserFindTagException


def get_response(session, url):
    """
    The function of loading the page with an exception.
    """

    try:
        response = session.get(url) 
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'An error occurred while loading the page {url}',
            stack_info=True
        )



def find_tag(soup, tag, attrs=None):
    """
    The tag search function, with an exception.
    """

    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag 
