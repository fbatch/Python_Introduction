# №3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
a = input('Введите своё число:\n')
result = int(a) + int(str(a) + str(a)) + int(str(a) + str(a) + str(a))
print(result)
