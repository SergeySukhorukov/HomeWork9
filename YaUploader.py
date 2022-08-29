import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': file_path, 'overwrite': 'true'}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        response = requests.get(url, headers=headers, params=params).json()
        href = response.get('href', '')
        res = requests.put(href, data = open(file_path, 'rb'))
        if res.status_code == 201:
            print('Загрузка прошла успешно!')
        else:
            print(f'Ошибка загрузки! Код ошибки: {res.status_code}')

