"""""
sum = 0
counter =1
while counter <=100:
    sum=sum+counter
    print(sum)
    counter+=1
print('1到100之加總:',sum)
"""
"""""
for n in range(2,20):
    x=2
    while x<n:
        if n %x ==0:
            print(n,'可被',x,'整除')
            break
        x+=1
    else:
        print(n,'是質數')
"""

birthdays={'alice':'0401','bob':'0808','carol':'1212'}
""""
while True:
    print('enter a name:(blank to quit)')
    name= input()
    if name =='':
        break

    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for'+name)
        print('what is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('birthday data updated')
        print(birthdays)
"""
"""""
condition=0
while condition<10:
    print(condition)
    condition+=1
"""




