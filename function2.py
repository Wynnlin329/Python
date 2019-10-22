'''''
def aaa():
    a='hello'
    b='10'
    c='20'
    d='30'
    return a,b,c,d

aaa()
print(aaa())
'''
'''''
def main():
    print('this is main function called')
    sub_function(10,20)

def sub_function(p1,p2):
    print('received value para1={}para={}'.format(p1,p2))

if __name__ == '__main__':
    main()
'''

def main():
    b='我是B'
    funtion_change_value(b)
    print(b)

#    b= funtion_change_vulue(b)
#    print(b)

#def funtion_change_value(a):
#    a='我是A'
#    print("------------")
#def funtion_change_value(a):
#    a='我是回傳的A'
#    return a

#if __name__ == '__main__':
#    main()

'''''
def main():
    b=['我','是','B']
    print(b)
    function_change_value(b)
    print(b)
    
def function_change_value(a):
    a[0]='換'
    a[1]='成'
    a[2]='A'

main()
'''
'''''
def main():
    c=999
    print_info(5,b=10)

def print_info(a,*,b):
    print(a+b)
    print(c)
main()
'''
'''''
flag =10
def main():
    function_a()
    print(flag)
def function_a():
    flag = 20
  
    def set_flag():
        flag=30
    set_flag()
    print(flag)
main()
'''
'''''
def main():
    print(list(my_range(10)))
    g=my_range(9)
    print(next(g))
    print(next(g))

def my_range(n):
    x=0
    i=1
    g=1
    while True:
        yield x
        x = i + x
        yield i
        i =i+x
        g+=1
        if g==n:
            break
main()
'''

#week_day=['星七一','星期二','稀奇三','西情似','星期五','星期六','星期日']

#for day in iter(week_day):
#    print(day)
#print('')
#for i in range(len(week_day)):
#    print(week_day[i])
#print('')
#for day in iter(list(reversed(week_day))):
#    print(day)
'''''
def add_ten(x):
    x+=10

def add_ten_r(x):
    return x+10

def main():
    l=[1,2,3,4,5,6]
    m=map(lambda x:x*10,l)

    print(m)
    print(list(m))

    n=list(map(add_ten,l))
    print(n)
    n=list(map(add_ten_r,l))
    print(n)
main()
'''

animals=['bat','rat','elephant','cat']
for item in animals:
    print(animals.index(item))
print(animals.index('rat'))