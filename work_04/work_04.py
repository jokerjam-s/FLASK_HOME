import argparse
import os
import threading
import time
from multiprocessing import Process, Pool
import asyncio

import requests


def load_thread(url_list: list, path: str):
    """Загрузка потоками"""
    threads = []
    for url in url_list:
        thread = threading.Thread(target=download, args=['thread_', url, path])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def load_process(url_list: list, path: str):
    """Загрузка процессами"""
    processes = []
    for url in url_list:
        process = Process(target=download, args=['process_', url, path])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


async def load_async(url_list: list, path: str):
    """Асинхронная загрузка"""
    tasks = []
    for url in url_list:
        task = asyncio.ensure_future(async_download(url, path))
        tasks.append(task)
    await asyncio.gather(*tasks)


def download(prefix: str, url: str, path: str):
    """
    Загрузка файла по url
    :param prefix: префикс имени файла
    :param url: ссылка для загрузки
    :param path: каталог назначения
    :return:
    """
    start_time = time.time()
    responce = requests.get(url)
    file_name = (path + prefix + url[url.rfind('/') + 1:])
    with open(file_name, "wb") as f:
        for buff in responce.iter_content(2048):
            if buff:
                f.write(buff)
    print(f'{url} загружен {time.time() - start_time:.2f} сек.')


async def async_download(url: str, path: str):
    """
    Асинхронная загрузка
    :param url: ссылка для загрузки
    :param path: каталог назначения
    :return:
    """
    start_time = time.time()
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, requests.get, url, {"stream": True})
    filename = (path + 'async_' + url[url.rfind('/') + 1:])
    with open(filename, "wb") as f:
        for buff in data.iter_content(2048):
            if buff:
                f.write(buff)
    print(f'{url} загружен {time.time() - start_time:.2f} сек.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Загрузка файлов из сети тремя способами')
    parser.add_argument('datafile', metavar='file', type=str, help='файл данных со списком файлов к загрузке')

    args = parser.parse_args()
    path_image = os.getcwd() + '\\img\\'

    with open(args.datafile, 'r', encoding='utf-8') as f:
        url_list = [line.strip() for line in f]

    print('---- THREAD ----')
    load_thread(url_list, path_image)
    print('---- PROCESS ----')
    load_process(url_list, path_image)
    print('---- ASYNC ----')
    asyncio.run(load_async(url_list, path_image))



