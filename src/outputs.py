import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT, OUTPUT_FILE, OUTPUT_TABLE


def control_output(results, cli_args):
    """
    The function of selecting the output of the results.
    """

    output = cli_args.output
    if output == OUTPUT_TABLE:
        pretty_output(results)
    elif output == OUTPUT_FILE:
        file_output(results, cli_args)
    else:
        default_output(results)


def default_output(results):
    """
    The function for displaying the result in a lowercase format.
    """

    for row in results:
        print(*row)


def pretty_output(results):
    """
    The function of displaying the result in a tabular format.
    """

    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    """
    The function of writing the result to a file.
    """

    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')
