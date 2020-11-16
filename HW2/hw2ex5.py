# Exercise 5
my_list = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))
for i in range(len(my_list)):
    if my_list[i] < a:
        my_list.insert(i, a)
        break
    elif a <= my_list[-1]:
        my_list.append(a)
        break
    else:
        continue
print(my_list)
