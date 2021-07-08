import requests
import io

""" Версия 20210706"""


class YandexDisk():

    def download_file(self, token, path='disk:') -> bytes:
        response = requests.get(
            url='https://cloud-api.yandex.net/v1/disk/resources/download',
            headers={'Authorization': f'OAuth {token}'},
            params={'path': f'disk:{path}', 'fields': 'href'})
        answer = response.json()['href']
        file = requests.get(url=answer).content
        return file

    def upload_file(self, token, path='disk:', file=None, overwrite=False):
        """
        Загрузка файла на ЯндексДиск
        @param token: oauth токен авторизации на Яндекс.Диск
        @type token: str
        @param path: путь до паки размещения файла на Янжекс.Диск
        @type path: str
        @param file: данные для записи в файл на Яндекс.Диск
        @type file: str
        @param overwrite: разрешить перезапись файла
        @type overwrite: bool
        @return:
        @rtype:
        """
        if type(file) == list:
            file = '\r\n'.join(file)
            file = file.encode()

        file = io.BytesIO(file)
        # print(f'{file=}')

        # Получить URL для загрузки файла
        response = requests.get(
            url='https://cloud-api.yandex.net/v1/disk/resources/upload',
            headers={'Authorization': f'OAuth {token}'},
            params={'path': f'disk:{path}', 'overwrite': overwrite})
        put_url = response.json()['href']

        # Загрузить данные по полученному URL
        response = requests.put(url=put_url, data=file)
        # print('def upload_json(self, file): - выполнен')
        return True


Yandex_Disk = YandexDisk()
