
def python99():
    print("python_01 簡介與城市漁鹽機處")
    print("python_02 簡介與城市漁鹽機處")
    print("python_03 簡介與城市漁鹽機處")
    print("python_04 簡介與城市漁鹽機處")
    print("python_05 簡介與城市漁鹽機處")
    print("python_06 簡介與城市漁鹽機處")
    print("python_07 簡介與城市漁鹽機處")

#python99()
''''
def calculater(num):
    i = 1
    r = 0
    while i<=num:
        r=r+i
        i+=1
    return r
'''
#result = calculater(79)
#print("%d"%result)
'''''
def printline():
    print('-'*50)

def printline_2(n):
    i=1
    while i<=n:
        printline()
        i+=1
    return n
    
'''
#num=int(input('請輸入數量'))
#result = printline_2(num)
def add3num(a,b,c):
    aaa=a+b+c
    bbb=a-b-c
    return aaa,bbb

#def dev3num([aaa],[bbb]):
#    g=add3num(a,b,c)/3
#    return g

#a = int(input('輸入A'))
#b = int(input('輸入B'))
#c = int(input('輸入C'))
#result = add3num(a,b,c)
#print(result)
'''
def divid(a,b):
    GG=a+b
    YY=a-b
    return GG,YY

PP,QQ = divid(1,2)
print(PP,QQ)
'''
'''''
def test(a,b,d,c=33):
    print(a)
    print(b)
    print(c)
    print(d)

test(11,22,55,)
'''
#不定長參數
'''''
def test(a,b,*args, **kwargs,):#*可放多序列() **字典
    print(a)
    print(b)
    print(args)
    print(kwargs)

G=[11,22,33]
T={'aa':100,'bb':200}

test(11,22,33,44,55,66,*G,**T)#*解序列 **解字典
'''

#aaa=lambda a:a+1

#print(aaa(8))

def test(a,b,xxx):
    return xxx(a,b)

result = test(11,22,lambda x,y:x+y)
print(result)
