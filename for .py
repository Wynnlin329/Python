"""""
sites=['facebook','google','amazon','twitter','youtube',
       'yahoo']

for site in sites:
    print('編號',sites.index(site),'站台'+site)
print('完成python for loop！')
"""

"""
sites=['facebook','google','amazon','twitter','youtube',
       'yahoo']

print('串聯長度:',len(sites))
print('串列範圍:',range(len(sites)))

for i in range(len(sites)):
    print('編號',i,'站台'+sites[i])
print('\n')

print('列出第二筆到第四筆:')

for i in range(2,5):
    print('編號',i,'站台'+sites[i])
"""
"""
sites=['facebook','google','amazon','twitter','youtube',
       'yahoo']
for i in range(len(sites)):
    print('編號',i,'站台'+sites[i])
    if sites[i]=='twitter':
        break
print('GG')
"""
"""
l=[0,1,2,3,4,5,6,7,8,9,10]

print('使用continue')
for item in l:
    if item==7:
        continue
    print(item)

print('\n使用pass')
for item in l:
    if item==7:
        pass
    print(item)
"""

"""""
for n in range(2,20):
    for x in range(2,n):
        if n%x==0:
            print(n,'可被',x,'整除')
            break
    else:
        print(n,'是質數')
"""

#print([x*2+10 for x in range(20)])

#print([x for x in range(22) if x %3 ==0])

