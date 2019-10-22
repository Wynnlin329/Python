#pip3 install flask-bootstrap flask-moment flask-wtf Flask-SQLAlchemy

from flask import Flask, render_template, request, jsonify,session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import  Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired,InputRequired,Length,NumberRange
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc,asc
from datetime import datetime
from flask_paginate import Pagination,  get_page_args

app = Flask(__name__)

#配置密鑰
app.config['SECRET_KEY'] = '-XQRl_yWcNaqrV5m'

# 配置資料庫連線
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://dbuser:aabb1234@localhost/my_test_db"

# 關閉動態追蹤修改的警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 展示sql語句
app.config['SQLALCHEMY_ECHO'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)

#資料庫物件
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),nullable=False)
    class_id = db.Column(db.Integer,  db.ForeignKey('product_class.id'), nullable=False,)
    price = db.Column(db.Integer, nullable=False, default=0 )
    counts = db.Column(db.Integer, nullable=False, default=0 )
    def __repr__(self):
        return '<Product {} {}>'.format(self.id,self.name)

class Product_Class(db.Model):
    __tablename__ = 'product_class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),nullable=False)
    def __repr__(self):
        return '<Product_Class {} {}>'.format(self.id,self.name)


#表單物件
class ProductForm(FlaskForm):
    product_name = StringField ('名稱',validators=[InputRequired(), Length(min=4,max=60)])
    product_class_list = [(row.id, row.name) for row in Product_Class.query.all()]
    product_class_list.insert(0, (-1, '請選擇'))
    product_class_id = SelectField('分類', coerce = int , choices=product_class_list,
                                   validators=[InputRequired(),NumberRange(min=1,message='請選擇分類')])
    product_price = IntegerField('價格',validators=[InputRequired(),NumberRange(min=0,message='價格請輸入0以上整數')])
    product_counts = IntegerField('數量',validators=[InputRequired(),NumberRange(min=0,message='數量請輸入0以上整數')])
    submit = SubmitField('送出')


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
        # elif form.errors and 'formData' in session:
        return render_template('404.html'), 404

@app.route('/new',methods=['GET','POST'])
def new_input():  #new_input為產生視圖(View)的函式
    # 建立產品表單物件
    form = ProductForm()

    #準備接收表單資料
    formData={
        'name' : None,
        'class_id' : None,
        'price' : None,
        'counts' : None
    }
    #表單錯誤訊息
    formError = None

    #資料操作訊息
    dbMsg = None

    #收到網頁表單送出的資料
    if form.validate_on_submit():
        formData ={
            'name' : form.product_name.data,
            'class_id' : form.product_class_id.data,
            'price' :  form.product_price.data,
            'counts' : form.product_counts.data
        }
        print(formData)
        try:
            new_product_data = Product(**formData)
            db.session.add(new_product_data)
            db.session.commit()
            dbMsg='新增資料成功!'
        except Exception as err:
            print(err)
            dbMsg ='資料新增失敗!'

    elif form.errors:
        formError = [str(form.errors[error])[2:-2] for error in form.errors]
        print(formError)

    # 繪製客端的網頁
    return render_template('product_form.html', form=form, formData=formData,formError=formError,dbMsg=dbMsg)

@app.route('/list',methods=['GET','POST'])
def product_list():

    colname = ['編號','名稱','分類','價格','數量','刪除','編輯']
    table_cols = [Product.id,Product.name,Product_Class.name,Product.price,Product.counts]
    sort_col_index = -1

    sort_type = request.args.get('type')
    sort_col_name = request.args.get('col')

    if sort_col_name:
        try:
            sort_col_index = colname.index(sort_col_name)
        except Exception as err:
            sort_col_index = -1
            print('sort_col_index err:',err)


    if sort_type == 'desc' and  sort_col_index in range(0,5) :
        rows = [[p.id, p.name, c.name, p.price, p.counts]
                for p, c in db.session.query(Product, Product_Class).
                    order_by(desc(table_cols[sort_col_index])).
                    filter(Product.class_id == Product_Class.id).all()
                ]
    elif sort_type == 'asc' and  sort_col_index in range(0,5):
        rows = [[p.id, p.name, c.name, p.price, p.counts]
                for p, c in db.session.query(Product, Product_Class).
                    order_by(asc(table_cols[sort_col_index])).
                    filter(Product.class_id == Product_Class.id).all()
                ]
    else:
        rows = [[p.id, p.name, c.name, p.price, p.counts]
                for p, c in db.session.query(Product, Product_Class).
                    filter(Product.class_id == Product_Class.id).all()
                ]

    #debug print(rows[0])

    #分頁 (pip install -U flask-paginate)
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    total = len(rows)

    pagination = Pagination(page=page, per_page=per_page, total=total, bs_version=4,
                            css_framework='bootstrap')


    print('page args:',get_page_args(page_parameter='page',
                                           per_page_parameter='per_page'))

    pagination_rows = rows[offset: offset + per_page]


    return render_template('product_list.html', colname=colname, rows=pagination_rows,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route('/update',methods=['GET','POST'])
def product_update():
    product_id = request.args.get('id')

    # 建立產品表單物件
    form = ProductForm()

    # 準備接收表單資料
    formData = {
        'name':  None,
        'class_id': None,
        'price': None,
        'counts':  None
    }
    # 表單錯誤訊息
    formError = None

    # 資料操作訊息
    dbMsg = None

    # 收到網頁表單送出的資料
    if form.validate_on_submit():
        formData = {
            'name': form.product_name.data,
            'class_id': form.product_class_id.data,
            'price': form.product_price.data,
            'counts': form.product_counts.data
        }
        print('update',formData)

        try:
            update_target = db.session.query(Product).filter(Product.id == product_id).first()
            update_target.name = form.product_name.data
            update_target.class_id = form.product_class_id.data
            update_target.price = form.product_price.data
            update_target.counts = form.product_counts.data
            db.session.commit()
            dbMsg = '更新資料成功!'
        except Exception as err:
            print(err)
            dbMsg = '資料更新失敗!'

    elif form.errors:
        formError = [str(form.errors[error])[2:-2] for error in form.errors]
        print(formError)

    # 繪製客端的網頁
    update_target = db.session.query(Product).filter(Product.id == product_id).first()
    form.product_name.data = update_target.name
    form.product_class_id.data = update_target.class_id
    form.product_price.data = update_target.price
    form.product_counts.data = update_target.counts

    return render_template('product_form.html', form=form, formData=formData, formError=formError, dbMsg=dbMsg)

@app.route('/delete')
def product_delete():
    product_id = request.args.get('id')
    db.session.query(Product).filter(Product.id == product_id).delete()
    db.session.commit()
    return redirect(url_for("product_list")+'?per_page=3')

@app.route('/product/<info>', methods=['GET'])
def product_data_api(info):  #API
    if info =='data':
        data_content = [{
            'product_id':p.id,
            'product_name':p.name,
            'product_class_id':c.id,
            'product_class_name':c.name,
            'product_price':p.price,
            'product_counts':p.counts
            }for p, c in db.session.query(Product, Product_Class).filter(Product.id == Product_Class.id).all()]
        return jsonify(data_content)
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
