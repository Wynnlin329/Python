'''''
str_t='\'this is a python string.\''
for i in range(len(str_t)):
    print('str_t[',i,']=',str_t[i])

print(str_t[1:0])
print(str_t[:10])
print(str_t[10:17])
print(str_t[17:])
print(str_t[:10]+str_t[17:])
print(str_t[::3])
'''

#
# str_t='this is a python string.'
# print(str_t.split())
#
# str_p='alice,jor,bob,kent,zoey'
# print(str_p.split(','))
#
# print('/'.join(str_p.split(',')))
#
# str_a='''prthon can be east to pick up whether you \'re a first time programmer
#         or you\'re experienced with
#         other languages.'''
# print(str_a.split('\n'))

'''
str_t='        [Python is easy]             '
print('\''+str_t.lstrip()+'\'')
print('\''+str_t.rstrip()+'\'')
print('\''+str_t.strip()+'\'')

print(str_t.strip('['))
'''
'''''
str_p='python is east to learn,and simple to use'
print(str_p.find('to'))
print(str_p.rfind('to'))

print(str_p.count('to'))

str_m = str_p.replace('to','GG',str_p.count(''))
print(str_m)

print('to'in str_m)
print(str_m)
print('python'not in str_m)

print(str_p.startswith('python'))
print(str_p.endswith('.'))
'''
#字串檢查
'''
def input_check(input_str):
    print('\n')
    print(input_str)
    print('is space:',input_str.isspace())
    print('is a numberic or alpha:', input_str.isalnum())
    print('is numberic:', input_str.isnumeric())
    print('is decimal:', input_str.isdecimal())
    print('is digit:', input_str.isdigit())
    print('is alpha:', input_str.isalpha())
    print('is lower:', input_str.islower())
    print('is upper:', input_str.isupper())
    print('is title:', input_str.istitle())
    print('is ascii:', input_str.isascii())

input_check('吃飯')
input_check('123456')
input_check('100.01')
input_check('')
input_check(' ')
# '''
#48頁第二題
# class GiveMeFive:
#     def __iter__(self):
#         self.a=5
#         return self
#     def __next__(self):
#         x=self.a**2
#         self.a +=x
#         return x
# def main():
#     gm5=iter(GiveMeFive())
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
# if __name__ == '__main__':
#     main()

