import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT, FILE


def control_output(results, cli_args):
    """Выбор нужной функции вывода данных."""
    output = cli_args.output
    if output == FILE:
        OUTPUT_FORMAT[output](results, cli_args)
    else:
        OUTPUT_FORMAT[output](results)


def default_output(results):
    """Выводит сырые данные в консоль."""
    for row in results:
        print(*row)


def pretty_output(results):
    """Выводит данные в консоль и лог в форме таблицы."""
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)
    logging.info(table)


def file_output(results, cli_args):
    """Выводит данные в .csv файл."""
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


OUTPUT_FORMAT = {
    'pretty': pretty_output,
    'file': file_output,
    None: default_output
}
