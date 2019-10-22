f= open('print_out.txt','r',encoding='utf-8')
print('{:3d}'.format(f.tell()),end='')
print(f)
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
    print('{:3d}'.format(f.tell()),end='')
f.close()

