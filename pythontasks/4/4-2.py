cities = input('Введите список городов: ').split()

for city in cities[::2]:
    print(city)
