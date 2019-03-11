from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'We are the world and lets wiw how it goes'


if __name__ == '__main__':
    app.run()
