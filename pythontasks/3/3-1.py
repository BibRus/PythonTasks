a, b, c = map(float, input('Введите коэффициенты: ').split())

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print('НЕТ')
else:
    print('ДА')



