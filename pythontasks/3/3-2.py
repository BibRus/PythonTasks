m, n = map(int, input('Введите два целых значения: ').split())
print(m // n if m % n == 0 and n != 0 else m * n)
