
'''''
animals=['bat','rat','elephant','cat']
seprator=','

join_str=seprator.join(animals)
print(join_str)

splitlist= join_str.split(',')
print(splitlist)
'''
#pairs=['('+str(i)+','+str(j)+')' for i in range(0,3) for j in range(0,4)]
#print(pairs)

'''''
a_list=[1,2,4,5,6]
b_list=a_list

print(a_list)
print(b_list)

b_list[2]=8
print(b_list)
print(a_list)

print('a_list id:'+str(id(a_list)))
print('b_list id:'+str(id(b_list)))
'''
'''''
a_list=[1,2,4,5,6]
b_list=a_list.copy()
c_list=list(a_list)
d_list=a_list[:]

print(a_list)
print(b_list)
print(c_list)
print(d_list)

b_list[2]=10
c_list[2]=20
d_list[2]=30

print(a_list)
print(b_list)
print(c_list)
print(d_list)

print('a_list id:'+str(id(a_list)))
print('b_list id:'+str(id(b_list)))
print('c_list id:'+str(id(c_list)))
print('d_list id:'+str(id(d_list)))
'''
'''''
city_name_tuple =()
print(city_name_tuple)

city_name_tuple ='taoyuan',
print(city_name_tuple)
print(type(city_name_tuple))

city_name_tuple =('taoyuan')
print(city_name_tuple)
print(type(city_name_tuple))
'''
'''''
number_tuple=10,30,20,40,50,10,20,30
print('值組中20的數量:',number_tuple.count(20))

for number in number_tuple:
    print(number,'index:',number_tuple.index(number))
'''
'''''
animals =['bat','rat','elssdf']
print(id(animals))
others=['there','sjdiij']
print(id(others))
others.extend(animals)

others += '.'
print(id(others))
'''
'''''
custom_dict ={'alice':'0913001002','amy':'0910123456','john':'0970033586','bob':'0918845100'}
print(custom_dict)

char_dict={ch_index:chr(ch_index) for ch_index in range(80,90)}
print(char_dict)
print()
'''
'''''
fruits=['apple','orange','banana','gggggg','kkklkkkk']
print(id(fruits))
fruits_zh=['蘋果','橘子','香蕉','111']
print(id(fruits_zh))
fruits_dict =dict(zip(fruits_zh,fruits))
print(fruits_dict)
'''
'''''
custom_dict ={'alice':'0913001002','amy':'0910123456','john':'0970033586','bob':'0918845100'}
print(custom_dict['amy'])
'''
'''''
custom_dict_1 ={'alice':'0913001002','amy':'0910123456','john':'0970033586','bob':'0918845100'}
print('custom_dict_1 比數:',len(custom_dict_1))
print('custom_dict_1 比數:',id(custom_dict_1))
custom_dict_2 ={'alex':'0919001002','bally':'0917123455','frank':'0980233586','bobbb':'09144045100'}
print('custom_dict_2 比數:',len(custom_dict_2))
print('custom_dict_2 比數:',id(custom_dict_2))

custom_dict_1.update(custom_dict_2)
print(id(custom_dict_1))
'''
'''''
custom_dict ={'alice':'0913001002','amy':'0910123456','john':'0970033586','bob':'0918845100'}
print('pop:',custom_dict.pop('amy'))
print(custom_dict)
print('popitem:',custom_dict.popitem())
print(custom_dict)
if 'alice' in custom_dict:
    print(custom_dict['alice'])
'''
'''''
custom_dict ={'alice':'0913001002','amy':'0910123456','john':'0970033586','bob':'0918845100'}
dict_a=custom_dict
dict_b=custom_dict.copy()

dict_a['bob']=''
dict_b['amy']= ''
print('custom_dict',custom_dict)
print('dict_a',dict_a)
print('dict_b',dict_b)
'''

custom_dict ={'alice':'0913001002','amy':'0910123456','john':'0970033586','bob':'0918845100'}

for i in sorted(custom_dict):
    print(i,custom_dict[i])

a=list(custom_dict)
a.sort()
for name in a:
    print(name,'',custom_dict[name])

#custom_dict.sort()

