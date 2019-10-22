class My_Cart:
    def __init__(self):
        self.shopping_list = {}

    def add(self,name='',price=0, num =0):
        if len(name.strip())>0 and num > 0:
            self.shopping_list[name] = [price,num]
            print('add item ',name,' $',price,' num=',num)

    def drop(self,name=''):
        if  len(name.strip())>0 and name in self.shopping_list:
            del self.shopping_list[name]
            print('drop item ', name)

    def modify(self,name='',price=0, num =0):
        if len(name.strip())>0 and num >0 and name in self.shopping_list:
            self.shopping_list[name] = [price, num]
            print('modify item ',name, ' $',price, ' num=',num)

    def account(self):
        total = 0
        for name in self.shopping_list.keys():
            total += self.shopping_list[name][0]*self.shopping_list[name][1]
        print(total)
        return total

    def list(self):
        print(self.shopping_list)
