import requests
from YaUploader import YaUploader
import os
from datetime import date, timedelta

def superhero_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url).json()
    max_value = 0
    max_name = ""
    for string in response:
        if string['name'] == 'Hulk' or string['name'] == 'Captain America' or string['name'] == 'Thanos':
                if string['powerstats']['intelligence'] > int(max_value):
                    max_value = str(string['powerstats']['intelligence'])
                    max_name = string['name']
    print(f"Самый умный герой {max_name}, его разум составляет {max_value}")


def stackoferlow_questions ():
    twodayago = date.today() - timedelta(days=2)
    url = f"https://api.stackexchange.com/2.3/questions?fromdate={twodayago}&order=desc&sort=activity&tagged=Python&site=stackoverflow"
    response = requests.get(url).json()
    for string in response['items']:
        print(string['title'])


if __name__ == '__main__':
    superhero_request()
    path_to_file = os.path.join(os.getcwd(),)
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload('TestFile.txt')
    print("Вопросы stackowerflow за последние 2 дня с тэгом Python:")
    stackoferlow_questions()