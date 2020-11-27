earnings = int(input('Укажите выручку компании:\n'))
costs = int(input('Укажите издержки компании:\n'))
if earnings > costs:
    print('Фирма работает с прибылью.')
    profitability = (earnings - costs) / earnings
    print('Рентабельность компании:', profitability)
    num_of_workers = int(input('Сколько человек работает в компании?\n'))
    profitability_per_worker = int((earnings - costs) / num_of_workers)
    print('Прибыль фирмы в расчете на одного сотрудника равна', profitability_per_worker)
elif earnings == costs:
    print('Фирма работает в ноль.')
else:
    print('Фирма работает с убытком')

