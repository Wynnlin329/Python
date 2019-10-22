#pip3 install flask-bootstrap flask-moment flask-wtf

from flask import Flask, render_template, request,session
from flask_bootstrap import Bootstrap
from flask_moment import  Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from  wtforms.validators import DataRequired

from datetime import datetime

app = Flask(__name__)


#配置密鑰: 防止 CSRF（Cross-site request forgery）跨站請求偽造
# import secrets ; secrets.token_urlsafe(12)
app.config['SECRET_KEY'] = '-XQRl_yWcNaqrV5m'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField ('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')


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

@app.route('/new',methods=['GET','POST'])
def new_input():
    name = None
    form = NameForm()

    try:
        session_name = session['user_name']
    except:
        session_name = None

    if form.validate_on_submit():
        name = form.name.data
        session['user_name'] = name
        form.name.data= ''

    return render_template('new.html', form=form, name=name, session_name=session_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
