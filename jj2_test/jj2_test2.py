from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    drinks=['Coffee','Coke','Green Tea','Water']
    return render_template('flow.html',name=name, drinks=drinks)

if __name__ == '__main__':
    app.run()