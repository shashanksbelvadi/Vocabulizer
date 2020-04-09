from decouple import config
import requests


def get_response(word_id):
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/en-us/' + word_id.lower()
    response = requests.get(url, headers={'app_id': config('app_id'), 'app_key': config('app_key')})

    return response
