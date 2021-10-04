number = list(input('Введите семизначное целое положительное число: '))
result = [int(digit) for digit in number]
print(' '.join(digit for digit in number))
