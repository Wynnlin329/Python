from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#建立與 product表格 對應的 Product物件
Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    pid = Column(Integer, primary_key=True)
    name = Column(String(60))
    price = Column(Integer)

#建立與資料庫的連線(session)
engine = create_engine('mysql://dbuser:aabb1234@localhost/my_demo_db', echo=False)
DBSession = sessionmaker(bind=engine) #sessionmaker建立一個 DBsession類別
session = DBSession() #將DBsession類別實體化成為session物件

print('列出全部的產品')
for row in session.query(Product):
    print(row.pid, row.name, row.price)

print('列出價格大於6000的產品')
for row in session.query(Product).filter(Product.price>6000):
    print(row.pid, row.name, row.price)

session.close()

