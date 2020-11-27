winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
a = int(input('Введите целое число от 1 до 12: '))
while a < 1 or a > 12:
        a = int(input('Пожалуйста, введите целое число от 1 до 12: '))
if a in winter:
    print('Зима')
elif a in spring:
    print('Весна')
elif a in summer:
    print('Лето')
else:
    print('Осень')
