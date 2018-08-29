import utils
import json


class Word(object):

    def __init__(self, word):
        self.word = word


    def get_definition(self):
        callable_url = utils.get_callable_url(self.word)
        response = utils.get_response(callable_url)

        return json.dumps(response.json())
