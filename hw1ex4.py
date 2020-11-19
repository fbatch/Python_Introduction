#4 Найдите самую большую цифру в числе
a = int(input('Введите целое положительное число:\n'))
while a:
    if a <= 0:
        print('Вы ввели не положительное число. Попробуйте еще раз.')
        a = int(input('Введите целое положительное число:\n'))
    if a > 0:
        max_num = 0
        while a != 0:
            i = a % 10
            if i >= max_num:
                max_num = i
            a //= 10
        print(max_num)
        break
