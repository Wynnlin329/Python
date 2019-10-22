import MySQLdb
#================select語法================
# #建立連線
# db = MySQLdb.connect(host='localhost',user='dbuser',passwd='aabb1234',
#                      db='my_demo_db', port=3306, charset='utf8')
# cursor = db.cursor() #建立游標
#
# try:
#     sql_str='select * from product' #select語法
#     cursor.execute(sql_str)
#     datarows = cursor.fetchall()
#     print(cursor.rowcount)
#     for row in datarows:
#         print(row)
#
# except Exception as err:
#     print('unable to fetch data from db')
#     print(err)
# db.close()
#================================
#================語法================
# db = MySQLdb.connect(host='localhost',user='dbuser',passwd='aabb1234',
#                      db='my_demo_db', port=3306, charset='utf8')
# cursor = db.cursor() #建立游標
# db.autocommit(True)
# try:
#     #sql_str='insert into product(name,price) values(\'{}\',{});'.format('Nokia 7',7000) #新增
#     #sql_str = 'update product set name=\'{}\' ,price={} where pid={} ;'.format('Nokia 6 Plus', 3200, 10)#修改
#     sql_str = 'delete from product where pid={} ;'.format(10)#刪除
#
#     cursor.execute(sql_str)
#
# except Exception as err:
#     print('unable to insert data to db')
#     print(err)
#
# #select語法 檢查結果
# try:
#     sql_str='select * from product where price > 3000;'
#     cursor.execute(sql_str)
#     datarows = cursor.fetchall()
#
#     for row in datarows:
#         print(row)
# except:
#     print('unable to fetch data from db')
#
# db.close()
#+++++++++++++ORM框架+++++++++++++++++++++++++++

