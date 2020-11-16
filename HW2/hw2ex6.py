# Exercise 6
name_1 = input('Введите название первого товара: ')
name_2 = input('Введите название второго товара: ')
name_3 = input('Введите название третьего товара: ')

price_1 = int(input(f'Введите цену товара под названием {name_1}: '))
price_2 = int(input(f'Введите цену товара под названием {name_2}: '))
price_3 = int(input(f'Введите цену товара под названием {name_3}: '))

quantity_1 = int(input(f'Введите количество товара под названием {name_1}: '))
quantity_2 = int(input(f'Введите количество товара под названием {name_2}: '))
quantity_3 = int(input(f'Введите количество товара под названием {name_3}: '))

units_1 = input(f'Введите единицу измерения товара под названием {name_1}: ')
units_2 = input(f'Введите единицу измерения товара под названием {name_2}: ')
units_3 = input(f'Введите единицу измерения товара под названием {name_3}: ')

name = 'название'
price = 'цена'
quantity = 'количество'
unit = 'единицы измерения'

tuple_1 = (1, {name: name_1, price: price_1, quantity: quantity_1, unit: units_1})
tuple_2 = (2, {name: name_2, price: price_2, quantity: quantity_2, unit: units_2})
tuple_3 = (3, {name: name_3, price: price_3, quantity: quantity_3, unit: units_3})

goods = [tuple_1, tuple_2, tuple_3]

print(f'\nСтруктура данных Товары: {goods}\n')

# Data analysis

if (units_1 == units_2) and (units_2 == units_3):
    unit_total = units_1
else:
    unit_total = [units_1, units_2, units_3]

my_dict = {name: [name_1, name_2, name_3], price: [price_1, price_2, price_3], quantity: [quantity_1, quantity_2, quantity_3], unit: unit_total}
print(f'Аналитика об имеющихся товарах: {my_dict}')
