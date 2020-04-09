from decouple import config
import requests


def get_response(word_id):
    url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + 'en' + '/' + word_id.lower()
    response = requests.get(url, headers={'app_id': config('app_id'), 'app_key': config('app_key')})
    print(config('app_id'))
    print(config('app_key'))

    return response
