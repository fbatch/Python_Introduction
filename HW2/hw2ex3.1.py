a = int(input('Введите целое число от 1 до 12: '))
my_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
while a < 1 or a > 12:
        a = int(input('Пожалуйста, введите целое число от 1 до 12: '))
for m in my_dict.keys():
    if a in my_dict.get(m):
        print(f"It's {m}!")
