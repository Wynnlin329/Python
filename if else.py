#a=input('請輸入一個整數:')
#c=int(a)
#if c>100:
#    print('您輸入的整數超過100')
#print('您輸入的是:'+a)

"""""
a=input("請輸入一個整數:")
c=int(a)
if(c % 2 )==0:
    print(c,'是偶數')
else:
    print(c,'是奇數')
"""

"""""
A=int(input('請輸入數字a:'))
B=int(input('請輸入數字b:'))

if A==B:
    print('數字A等於數字B')
elif A<B:
    print('數字A小於數字B')
else:
    print('數字A大於數字B')
"""

str_t ="alice , joe , bob , kent , zoey"
str_r =''
for item in str_t.split(' , '):
    str_r += item[0:-1] + item[-1].upper() +' '
print(' , '.join(str_r.split()))