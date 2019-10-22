"""""
for i in range(0,101):
    if i%2==0:
        print(i)
"""

area={'100':'台北市中正區','103':'台北市大同區','104':'台北市中山區',
      '105':'台北市松山區','106':'台北市大安區','108':'台北市萬華區',
      '110':'台北市信義區',}

while True:
    print('請輸入郵遞區號:')
    name = input()
    if name =='':
        break
    if name in area:
        print(area[name])




