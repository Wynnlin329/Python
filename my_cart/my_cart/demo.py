
from my_cart import *

def main():
    c = My_Cart()
    c.add('apple',30,1)
    c.add('juice',10,12)
    c.modify('juice',22,10)
    c.add('cookie',40,2)
    c.drop('apple')
    c.list()
    c.account()
if __name__ == "__main__":
    main()