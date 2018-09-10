import utils
import json
import constants
from dict_utils import DictUtils


class Word(DictUtils):

    def __init__(self, word):
        self.word = word
        self.entries = []

    def parse_response(self, response):
        lexical_entries = json.loads(response.text)[constants.RESULTS][0][constants.LEXICAL_ENTRIES]

        for entry in lexical_entries:
            entry_properties = {}
            senses = map(lambda e: e.get(constants.SENSES), entry.get(constants.ENTRIES))
            definitions = []
            short_definitions = []
            for sens in senses:
                nested_defs = map(lambda s: s.get(constants.DEFINITIONS, []), sens)
                nested_short_defs = map(lambda s: s.get(constants.SHORT_DEFINITIONS, []), sens)
                for n_d in nested_defs:
                    definitions.extend(n_d)
                for n_sd in nested_short_defs:
                    short_definitions.extend(n_sd)

            entry_properties[constants.DEFINITION_HEADER] = definitions
            entry_properties[constants.SHORT_DEFINITION_HEADER] = short_definitions
            entry_properties[constants.LANGUAGE_HEADER] = entry.get(constants.LANGUAGE)
            entry_properties[constants.PRONUNCIATION_HEADER] = entry.get(constants.PRONUNCIATIONS)

            self.entries.append(entry_properties)

    def get_definitions(self):
        json_response = {}
        response = utils.get_response(self.word)

        if response.status_code == 200:
            self.parse_response(response)

            return json.dumps(self.entries)
        elif response.status_code == 404:
            json_response[constants.MESSAGE] = 'The word ' + self.word + ' was not found in the dictionary.'
        else:
            json_response[constants.MESSAGE] = 'Something went wrong, please try again.'

        json_response[constants.STATUS_CODE] = response.status_code

        return json.dumps(json_response)
