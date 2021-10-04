expression = input('Введите выражение: ').split('+')

result = 0

for token in expression:
    if token != '+':
        result += int(token)

print(result)



