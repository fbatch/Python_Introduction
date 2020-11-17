# Exercise 5
def cool_function():
    a = input('Введите строку чисел через пробелы: ').split()
    total_sum = 0
    b = []
    c = []
    while not 'q' in a:
        for el in a:
            b.append(float(el))
            sub_sum = sum(b)
        total_sum += sub_sum
        print(f'Промежуточный результат: {sub_sum}, Общая сумма: {total_sum}')
        a = input('Введите строку чисел через пробелы: ').split()
    else:
        for el in a:
            q_index = int(a.index('q'))
            b = a[:q_index]
        for el in b:
            c.append(float(el))
            sub_sum = sum(c)
        total_sum += sub_sum
        print(f'Промежуточный результат: {sub_sum}, Общая сумма: {total_sum}')

cool_function()