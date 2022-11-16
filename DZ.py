print('введите коэффициенты a, b, c')
a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
x1=(-b-D**0.5)/(2*a)
x2=(-b+D**0.5)/(2*a)
if D<0:
    print('нет вещественного решения')
elif D>0:
    print('x1=', x1)
    print('x2=', x2)
else:
    print('x=', x1)

