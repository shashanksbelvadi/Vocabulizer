from decouple import config
import requests


def get_callable_url(word):
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + config('language') + '/' + word.lower()

    return url


def get_response(url):
    response = requests.get(url, headers={'app_id': config('app_id'), 'app_key': config('app_key')})

    return response
