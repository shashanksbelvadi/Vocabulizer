from flask import Flask
from word import Word

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Word('Hello').get_definition()


if __name__ == '__main__':
    app.run(debug=True, use_evalex=False, use_reloader=True)
