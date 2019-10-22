#===============================
# import  os,shutil,glob
#
# if os.path.exists('test_dir'):
#     shutil.rmtree('test_dir')
#
# os.mkdir('test_dir')
#
# os.chdir('test_dir')
#
# print(os.path.abspath('test_dir'))
#
# shutil.copy('../test_1','test_copy.txt')
#
# os.listdir('.')
#
# print(glob.glob('te*'))
#===================================
#----------LIST存取CSV模組--------------
# import csv
# food_cal_list = [
#     ['種類','單位','重量(g)','熱量(卡)'],
#     ['白米飯','1碗',205,225],
#     ['意大利肉醬麵','1份',248,330],
#     ['白吐司','1片',25,75],
#     ['全麥吐司','1片',25,65],
#     ['花生醬','1湯匙',16,95]
# ]
# print(food_cal_list)
#
# with open ('food_cal.csv',mode='w',newline='',encoding='utf-8')as csv_file:
#     writer=csv.writer(csv_file)
#     writer.writerows(food_cal_list)
#     writer.writerow(['果醬','1湯匙',18,50])
# print('write csv ok')
#
# with open('food_cal.csv',mode='r',newline='',encoding='utf-8')as csv_file:
#     rows = csv.reader(csv_file,delimiter=',')
#     print(rows)
    # read_csv_list = [row for row in rows]
    # print(read_csv_list)
#-------------------------------

#--------------字典存取CSV模組----

import csv
# dict_store_info = [{'門市':'民富門市','電話':'02 2514 0673','地址':'105台北市松山區民生東路四段130號'},
#                     {'門市':'延壽門市','電話':'02 2762 2884','地址':'105台北市松山區延壽街422號'},
#                     {'門市':'東鑫門市','電話':'02 2719 6327','地址':'105台北市松山區民生東路四段55巷10號'}
# ]
# dictrow = {'門市':'東急門市','電話':'02 2762 2908','地址':'105台北市松山區民生東路五段100號'}
#
# field_list = list(dict_store_info[0].keys())
# with open('dict_out.csv','wt',newline='',encoding='utf-8')as csvfile:
#     writer = csv.DictWriter(csvfile,fieldnames=field_list)
#     writer.writeheader()
#     writer.writerows(dict_store_info)
#     writer.writerow(dictrow)
#
#
dict_read_info =[]

with open('dict_out.csv','r',newline='',encoding='utf-8')as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        field_list = list(row.keys())
        #print(field_list)
        dict_read = {}
        for field in field_list:
            dict_read[field] = row[field]
        dict_read_info.append(dict_read)
        #print(dict_read_info)
for item in dict_read_info:
    print(item)


#------------------------------
#-----------pickle模組---------
# import pickle
# data = [12345,'hello','你好',{'臉書':'Facebook','google':'股歌'}]
#
# with open('out.pk','wb') as f:
#     pickle.dump(data,f)
#
# with open('out.pk','rb') as FF:
#     print(FF)
#     load_data= pickle.load(FF)
# print(load_data)
#-----------------------------
#-----------QR code----------
# import qrcode
#
# data = 'https://github.com/python/peps/blob/master/pep-0001.txt'
#
# img = qrcode.make(data=data)
#
# img.show()

#----------------------------

#------61頁第一題--------------
# from json import loads
# from urllib import request,parse
# url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-063'
# parms = {'Authorization':'CWB-7E625E4F-7BB2-43F1-9D45-DBB267018C1A'}
# querystring = parse.urlencode(parms)
#
# print(querystring)
# u = request.urlopen(url+'?' + querystring)
# resp = dict(loads(u.read()))
# print(resp['records'])
#-------------------------------------

# for n in range(1, 10):
#     for y in range(2, 6):
#         print('{}{}{}={:<2d}  '.format(y, 'X', n, n * y), end='', file=open('9x9.txt', 'a', encoding='utf-8'))
#     print(file=open('9x9.txt', 'a', encoding='utf-8'))
# # print('\n''{}{}{}={:<2d}  '.format(y,'X',n,n*y),end='',file=open('9x9.txt','a',encoding='utf-8'))
# print('',file=open('9x9.txt', 'a', encoding='utf-8'))
# for n in range(1, 10):
#     for y in range(6, 10):
#         print('{}{}{}={:<2d}  '.format(y, 'X', n, n * y), end='', file=open('9x9.txt', 'a', encoding='utf-8'))
#     print(file=open('9x9.txt', 'a', encoding='utf-8'))


#print(qq,file=open('9x9.txt','a',encoding='utf-8'))
#print('ok')

