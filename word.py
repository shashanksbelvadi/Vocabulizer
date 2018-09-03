import utils
import json


class Word(object):

    def __init__(self, word):
        self.word = word

    def get_definition(self):
        response = utils.get_response(self.word)

        if response.status_code == 200:
            return json.dumps(response.json())
        elif response.status_code == 404:
            return json.dumps({'message': 'No such word found in dictionary.'})
        else:
            return json.dumps({'message': 'Something went wrong, please try again.'})