#===================OPERASI LOGIKA BOOLEAN============

#NOT
a = False
c = not a
print('data a = ', a)
print('========NOT')
print('data c = ', c)

#OR
print('=============OR==============')
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
#AND
print('=============AND==============')
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
#XOR
print('=============XOR==============')
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)