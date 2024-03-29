from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)


if __name__ == '__main__':
    app.run()