#取得命令參數=========
import sys
# print(sys.api_version)
#
# print(sys.argv)
# print('命令參數的數量',len(sys.argv))
# print('python程式路徑:',sys.argv[0])
#
# for i in range(1,len(sys.argv)):
#     print('命令參數',i,sys.argv[i])
#====================

#附加文字檔案，順便選擇要使用哪個參數檔案===
# if len(sys.argv)>1:
#     f = open(sys.argv[1], 'w' , encoding='utf-8')
# else:
#     f = open('wE.txt','w',encoding = 'utf-8')
#     print('no')
# my_text = '''
# ['C:/Users/Big data/PycharmProjects/untitled/輸入與輸出.py', 'text.txt', 'file.txt']
# 命令參數的數量 3
# python程式路徑: C:/Users/Big data/PycharmProjects/untitled/輸入與輸出.py
# 命令參數 1 text.txt
# 命令參數 2 file.txt
# '''
#
# f.write(my_text)
# print('ok')
# f.close
#========================


# f = open('data', 'r', encoding='utf-8')
# line = f.readline()
#
# print(content)
# f.close()

# text = '''What is a PEP?
# ==============
#
# PEP stands for Python Enhancement Proposal.  A PEP is a design
# document providing information to the Python community, or describing
# a new feature for Python or its processes or environment.  The PEP
# should provide a concise technical specification of the feature and a
# rationale for the feature.'''
#
# print(text,end='',file=open('wE.txt','a',encoding = 'utf-8'))
# print('ok')

#----WITH----------
# food_cal_list = [
#     ['種類','單位','重量(g)','熱量(卡)'],
#     ['白米飯','1碗',205,225],
#     ['意大利肉醬麵','1份',248,330],
#     ['白吐司','1片',25,75],
#     ['全麥吐司','1片',25,65],
#     ['花生醬','1湯匙',16,95],
#     ['果醬','1湯匙',18,50],]
#
# with open('food_cal_csv',mode='w',encoding='utf-8')as f:
#     for line in range(len(food_cal_list)):
#         text = str(food_cal_list[line])\
#         .replace('[','').replace(']','').replace("\'",'')+'\n'
#         f.write(text)
#     else:print("ok")
#------------

