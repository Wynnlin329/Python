#pip3 install flask-bootstrap flask-moment flask-wtf

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import  Moment
from datetime import datetime

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return render_template('index.html',cur_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    if name =='yc':
        v1=request.args.get('v1')
        v2=request.args.get('v2')
        return render_template('user.html',name=name,v1=v1,v2=v2)
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
