""""
for y in range(1,10):
    for x in range(2,6):
        print('{}{}{}={:<2d} '.format(x,'x',y,x*y),end='')
    print('')

print('')

for y in range(1,10):
    for x in range(6,10):
        print('{}{}{}={:<2d} '.format(x,'x',y, x*y),end='')
"""
#n=2
"""""
for n in range(1,10):
    for y in range(2,6):
        print('{}{}{}={:<2d}  '.format(y,'X',n,n*y),end='')
    print('')
print('')

for n in range(1,10):
    for y in range(6,10):
        print('{}{}{}={:<2d}  '.format(y,'X',n,n*y),end='')
    print('')
"""

#print('{0:5}'.format(s))
'''''''''
i=1
n=1
while i <=100:
    n=i*n
    i+=1
print(n)
#print(i)
'''''''''''''''
def test (a):
    if a>1:
        return a*test(a-1)
    else:
        return a

result=test(10)
print(result)







