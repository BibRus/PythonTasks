students = tuple(input('Введите имена студентов: ').split())
mark = 'ва'

for student in students:
    if mark in student:
        print(student, end=' ')
