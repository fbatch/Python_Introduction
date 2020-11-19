# №6 Спортсмен, бег...
a = int(input('Введите результат в первый день (в километрах):\n'))
b = int(input('Введите вашу цель (в километрах):\n'))
counter = 1
while a < b:
    a = 1.1 * a
    counter += 1
print(counter)
