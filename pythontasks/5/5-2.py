numbers = list(map(int, input('Введите список целых чисел: ').split()))
N = int(len(numbers) ** 0.5)
matrix = [[numbers[row * N + column] for column in range(N)] for row in range(N)]
print(matrix)
