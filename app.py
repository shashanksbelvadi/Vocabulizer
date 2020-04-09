from flask import Flask, request, render_template
from word_util import WordUtil
import constants
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/define', methods=['GET', 'POST'])
def define():
    word_req = ''

    if request.method == 'POST':
        result = request.form
        word_req = result.getlist('search_param')[0].lower()
    elif request.method == 'GET':
        word_req = request.args.get('word')

    if not word_req:
        return json.dumps({constants.MESSAGE: 'Bad input; query word missing.'})

    definition_entries = json.loads(WordUtil(word_req).get_definitions())

    return render_template('define.html', keyword=word_req, entries=definition_entries)


if __name__ == '__main__':
    app.run(debug=True, use_evalex=False, use_reloader=True)
