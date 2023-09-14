import argparse
import os


def load_thread(files_list:list, path: str):
    """Загрузка потоками"""
    pass


def load_process(files_list:list, path: str):
    """Загрузка процессами"""
    pass


def load_async(files_list:list, path: str):
    """Асинхронная загрузка"""

    pass


def download(prefix: str, url:str, path: str):
    """
    Загрузка файла по url
    :param prefix: префикс имени файла
    :param url: ссылка для загрузки
    :param path: каталог назначения
    :return:
    """
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Загрузка файлов из сети тремя способами')
    parser.add_argument('datafile', metavar='file', type=str, help='файл данных со списком файлов к загрузке')

    args = parser.parse_args()
    path_image = os.getcwd() + '/img'

    file_list = None
    with open(args.datafile, 'r', encoding='utf-8') as f:
        file_list = [line.strip() for line in f]

    load_thread(file_list)
    load_process(file_list)
    load_async(file_list)
