from flask import Flask, request
from word import Word
import constants
import json

app = Flask(__name__)


@app.route('/define', methods=['GET'])
def define():
    word_req = request.args.get('word')

    if not word_req:
        return json.dumps({constants.MESSAGE: 'Bad input; query word missing.'})

    return Word(word_req).get_definitions()


if __name__ == '__main__':
    app.run(debug=True, use_evalex=False, use_reloader=True)
