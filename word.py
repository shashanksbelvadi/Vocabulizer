import utils
import json


class Word(object):

    def __init__(self, word):
        self.word = word
        self.entries = []

    def parse_response(self, response):
        lexical_entries = json.loads(response.text)['results'][0]['lexicalEntries']

        for entry in lexical_entries:
            entry_properties = {}
            senses = map(lambda e: e.get('senses'), entry.get('entries'))
            definitions = map(lambda s: s.get('definitions'), senses)

            entry_properties['definitions'] = definitions
            entry_properties['language'] = entry.get('language')
            entry_properties['pronunciations'] = entry.get('pronunciations')

            self.entries.append(entry_properties)

    def get_definitions(self):
        json_response = {}
        response = utils.get_response(self.word)

        if response.status_code == 200:
            self.parse_response(response)

            return json.dumps(self.entries)
        elif response.status_code == 404:
            json_response['message'] = 'The word ' + self.word + ' was not found in the dictionary.'
        else:
            json_response['message'] = 'Something went wrong, please try again.'

        json_response['status_code'] = response.status_code

        return json.dumps(json_response)
