'''
try:
    10 * (1/0)
    print(a)
    b= [1,2,3]
    print((b[5]))
    c = 1
    print('c='+c)

except ZeroDivisionError :
    print('攔截到\'除以0\'的錯誤')
    raise
except NameError:
    print('攔截到使用未宣告變數的錯誤')
except IndexError:
    print('攔截到存取串列索引值超過範圍的錯誤')
except:
    print('攔截到其他錯誤')
else:
    print('都沒有出現例外，會進到這裡')
finally:
    print('最後都會進到這裡')

'''

# def boxprint(symbol,width,height):
#     if len(symbol) !=1:
#         raise Exception('symbol must be a single character string')
#     if width <=2:
#         raise Exception('width must be greater than 2.')
#     if height <=2:
#         raise Exception('CCCCCCCC')
#
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2 ))+ symbol)
#     print(symbol * width)
#
# for sym,w,h in (('*',3,3), ('@',6,4),('x',1,3),('zz',3,4)):
#     try:
#         boxprint(sym,w,h)
#     except Exception as err:
#         print('An exception happened:'+str(err))




'''
try:
    buget=6000
    while(True):
        cost_of_month = input('請輸入每月花費:')
        if cost_of_month.strip() == '':
            break
        assert int(cost_of_month)<= buget ,'the cost is over buget'
except AssertionError as err:
    print('Assertion Error' + str(err))

'''
def boxprint(symbol,width,height):
    if len(symbol) !=1:
        assert len(symbol) <2,('symbol must be a single character string')
    if width <=2:
        assert width >2 ,('width must be greater than 2.')
    if height <=2:
        assert height >2 ,('CCCCCCCC')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2 ))+ symbol)
    print(symbol * width)

for sym,w,h in (('*',3,3), ('@',6,4),('x',1,3),('zz',3,4)):
    try:
        boxprint(sym,w,h)
    except Exception as err:
        print('An exception happened:'+str(err))
