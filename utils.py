from decouple import config
import requests


def get_response(word_id):
    url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + 'en' + '/' + word_id.lower()
    response = requests.get(url, headers={'app_id': '01f441e0', 'app_key': 'cc85bf3d958d316f86140d34370369ec'})

    return response
