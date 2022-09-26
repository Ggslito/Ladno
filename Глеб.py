'''a = int(input('Введите число:'))
b = int(input('Введите степень числа:'))
c = pow(a,b)
print(c)'''
a = input('Введите средний ряд:')
b = int(input('JCYJDFYBT(основание):'))
c = list(a)
c.reverse()
res = 0
for x in range(len(a)):
    res = res + (int(b)**x)*int(c[x])
print(res)