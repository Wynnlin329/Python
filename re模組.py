'''''
import re
ret_match= re.match(r'^\d{4}-\d{2}-\d{2}$','1988-07-25')

if(ret_match):
    print('ret_match:',ret_match)
    print('ret_match:',ret_match.group())

else:
    print('net_match:none')
'''''
'''
import re
input_str='terry,1983-04-05, marry,1985-07-22, joe,1978-05-22'
ret_search=re.search(r'\d{4}-\d{2}-\d{2}',input_str)

if(ret_search):
    print('ret_ssssss:',ret_search)
    print('ret_ssss:',ret_search.group())
else:
    print('retsssssss  none')


'''
#ret_search=re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)',input_str)
'''''
if (ret_search):
    print('ret_search:', ret_search.groups())
    print('ret_search:', ret_search.group())
    print('ret_search:', ret_search.group(1))
    print('ret_search:', ret_search.group(2))
    print('ret_search:', ret_search.group(3))
else:
    print("ret_search:none")
'''
#非貪婪
# import re
# input_str= 'A running <div>dog</div> raws a walking <dir>pig</div>.'
# ret_match=re.findall(r'<div>(.*?)</div>',input_str)
# if ret_match:
#     print(ret_match)
# else:
#     print('ret_match:none')

'''
import re
input_str= '(1) Jacky Wu (2) JayChou (3) JJ Lin'
ret_match = re.split(r'\(\d\)',input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match none")
'''

'''''
namelist="alice,joe,bob,kent,zoey"
namealice=namelist[4:5]
namejoe=namelist[6:7]
namebob=namelist[12:13]
namekent=namelist[17:18]
namezoey=namelist[22:23]
namealice_E=namealice.title()
namejoe_J=namejoe.title()
namebob_B=namebob.title()
namekent_T=namekent.title()
namezoey_Y=namezoey.title()
print('alic{},jo{},bo{},ken{},zoe{}'.format(namealice_E,namealice_E,namebob_B,namekent_T,namezoey_Y))
#,namejoe_J,namealice_E,namebob_B,namekent_T,namezoey_Y
#,'%so%s','bo%s','ken%s','zoe%s'
'''

'''''
import re
aaa="a4485484548,A123456789,d154545454,E1212121211"
ret_search=re.search(r'([A-Za-z])(\d\d\d\d\d\d\d\d\d)\b',aaa)
if(ret_search):
    print(ret_search)
else:
    print('noe')
'''

#
# namelist="alice,joe,bob,kent,zoey"
# a=namelist[::-1]
# print(a)
# aa=a.title()
# print(aa)
# aaa=aa[::-1]
# print(aaa)
#
#32第二題

# import re
# a= 'python is east to learn,easy to write and simple to use.'
# b=re.findall(r'(to)',a)
# print(b)