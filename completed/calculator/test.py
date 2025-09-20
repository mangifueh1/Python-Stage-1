dis = '22+2+2+4'
num = dis.split('+')
total = 0
for i in num:
    total = int(i) + total

print(total)
