###############################################################################           
# Mohammd-AlKharaan-Assignment02
#
# CPS 202 Assignment #02
# Mohammd AlKharaan
#
# Larger Programq    


from Currency import *

a = Currency(1000, 'SAR')
b = a.convert_to('USD')
b1 = a.convert_to('EUR')
b2 = a.convert_to('JPY')
b3 = a.convert_to('AUD')
b4 = a.convert_to('CAD')
b5 = a.convert_to('CNY')
b6 = a.convert_to('GBP')
c = Currency(10000, 'CAD')
d = c.convert_to('USD')
e = a + 5.544
f = c + 154
e1 = a - 5.544
f1 = c - 154
e2 = 5.544 - c
f2 = 154 - a
f3 = a + c
f4 = c + a

print('a is', a)
print('c is', c)
print('c converted to USD is ', d)
print()
print(a,'is' ,b)
print(a,'is' ,b1)
print(a,'is' ,b2)
print(a,'is' ,b3)
print(a,'is' ,b4)
print(a,'is' ,b5)
print(a,'is' ,b6)
print()
print(a,'+ 5.544 =', e)
print(c,'+ 154 =', f)
print(a,'- 5.544 =', e1)
print(c,'- 154 =', f1)
print('5.544 - c =', e2)
print('154 - a =', f2)
print(a, '+',c, '=',f3)
print(c,'+',a, '=', f4)
print()
print( a,' > ',c ,a > c )
print( a,' < ',c, a < c )
print(c, ' > ',a, c > a )
print( c,' < ',a, c < a )
