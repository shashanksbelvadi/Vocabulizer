import constants


class WordEntry:
    pronunciations = {}
    senses = {}

    def __init__(self, **kwargs):
        self.make_pronunciations(kwargs.get(constants.PRONUNCIATIONS))
        self.make_senses(kwargs.get(constants.SENSES))

    def make_pronunciations(self, pronunciation_list: list):
        for pronunciation in pronunciation_list:
            self.pronunciations[constants.AUDIO_FILE] = pronunciation.get(constants.AUDIO_FILE)
            self.pronunciations[constants.DIALECTS] = pronunciation.get(constants.DIALECTS)[0]

    def make_senses(self, sense_list: list):
        for sense in sense_list:
            self.senses[constants.DEFINITIONS] = sense.get(constants.DEFINITIONS)
            self.senses[constants.EXAMPLES] = sense.get(constants.EXAMPLES)
