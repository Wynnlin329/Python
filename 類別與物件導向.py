#類別定義
'''''
class Car:
    year = 2019
    mpg=30
    speed=0
    def accelerate(self,):
        self.speed += 20
    def brake(self):
        self.speed -= 10


def main():
    car1=Car()
    print('speed',car1.speed)
    car1.accelerate()
    car1.accelerate()
    print('speed',car1.speed)
    car1.brake()
    print('speed',car1.speed)

if __name__ == '__main__':
    main()
'''









'''''
class Car:
    year = 2019
    mpg=30
    speed=0

    def __init__(self,speed):
        self.speed=50
    def accelerate(self):
        self.speed+=20
    def brake(self):
        self.speed-=10

def main():
    car1=Car(10)
    car2=Car(20)
    car1.accelerate()
    car1.accelerate()
    car2.accelerate()
    print('car1 speed',car1.speed)
    print('car2 speded',car2.speed)
if __name__ =='__main__':
    main()
'''
#類別方法
'''''
class Car:
    year = 2019
    mpg=30
    speed=0

    def __init__(self,speed):
        self.speed=speed
    def accelerate(self):
        self.speed+=20
    def brake(self):
        self.speed-=10

def main():
    Car.color='black'
    Car.brand='benz'
    car1=Car(15)
    car1.type='suv'

    print('car speed',car1.speed)
    print('car color',car1.color)
    print('car brand',car1.brand)
    print('car type',car1.type)
if __name__ =='__main__':
    main()
'''
#物件導向
'''''
class Book():
    def __init__(self,name='',author='',price=0):
        self.name = name
        self.author=author
        self.__price=0

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
       self.__price=value

def main():
    book1=Book('哈利波特神秘ㄉ魔法師','JK羅琳')
    print('書名:',book1.name)
    print('作者:',book1.author)
    book1.price=320
    print('售價:',book1.price, '$NTD')

if __name__ =='__main__':
    main()
'''

#類別內建方法(封裝)
class Book():
    def __init__(self,name='',author='',price=0):
        self.name = name
        self.author=author
        self.__price=price
    def __str__(self):
      return 'name:'+self.name+\
             'author,'+self.author+','\
             'price,'+str(self.__price)
    def __del__(self):
        print(self.name+'已經移除')
        print(self.__price,'已經移除')
    def __call__(self,name='',author='',price=0):
        if len(name.strip())>0:
            self.name=name
        if len(author.strip())>0:
            self.author=author
        if price>=0:
            self.__price =price
def main():
    book1=Book('哈利波特神秘的魔法石','JK羅琳',350)
    book1('哈利波特消失的秘施','',320)
    print(book1)
if __name__ =='__main__':
    main()


#繼承---------------------------------------

'''''
class Car:
    year=1990;  mpg=30000;  speed=0
    def __init__(self,year,mpg,speed):
        self.year=year
        self.mpg=mpg
        self.speed=speed
        print(year,mpg,speed)
    def accelerate(self):
        self.speed +=20
        print('speed up:',self.speed)
    def brake(self):
        self.speed-=10
        print('speed down:',self.speed)
        print(self.speed)
class RaceCar(Car):
    def __init__(self,color='',make='',engine='',year='',mpg=0,speed=0):
        self.color=color
        self.make=make
        self.engine=engine
        super(RaceCar,self).__init__(year,mpg,speed)
    def turbo_start(self):
        self.speed +=100
        print('turbo mode start speed:',self.speed)
    def brake(self):
        print('abs mode start')
        super().brake()

def main():
        my_car=RaceCar('white','nissan gtr','v6','2007',3000,0)
        print(my_car.color,my_car.make)
        my_car.accelerate()
        my_car.turbo_start()
        my_car.accelerate()
        my_car.brake()

if __name__== '__main__':
    main()
'''
'''''
class Base(object):
    def __init__(self):
        print('I am Base')
class A(Base):
    def __init__(self):
        print('I am A')
        super().__init__()
class B(Base):
    def __init__(self):
        print('I am B')
        super().__init__()
class C(A,B):
    def __init___(self):
        super().__init__()
def main():
    c=C()
if __name__ == '__main__':
    main()
'''

# class Vector3D:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self,other):
#         #print(other)
#         v = Vector3D(self.x + other.x,self.y + other.y,self.z)
#
#         return v
#     def __sub__(self, other):
#         v = Vector3D(self.x -other.x, self.y - other.y, self.z -other.z)
#         return v
#     # def __str__(self):
#     #     s = '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
#     #
#     #     return s
# def main():
#
#     v1 = Vector3D(1,2,3)
#     v2 = Vector3D(1,1,0)
#
#     print(type(v1-v2))
#     print(v1+v2)
#
# if __name__ == '__main__':
#     main()


# class GiveMeFive:
#     def __iter__(self):
#         self.a=5
#         return self
#     def __next__(self):
#         x=self.a
#         self.a*=x
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

#48頁第一題----------------------------------
# class Member():
#     def __init__(self,name=0,phone=0,email=0):
#         self.__name = name
#         self.__phone= phone
#         self.__email= email
#
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def phone(self):
#         return self.__phone
#     @property
#     def email(self):
#         return self.__email
#
#     @name.setter
#     def name(self,value):
#        self.__name=value
#     @phone.setter
#     def phone(self,value):
#        self.__phone=value
#     @email.setter
#     def email(self,value):
#        self.__email=value
#
# def main():
#     Member1=Member('李泓慶','0978787878','5#######@jjj.com')
#     # Member1.name='高聖翔'
#     # Member1.phone='0987878787'
#     # Member1.email='@@@@@@@@555.com'
#     print('姓名:',Member1.name)
#     print('電話:',Member1.phone)
#     print('信箱:',Member1.email)
#
# if __name__ =='__main__':
#     main()

