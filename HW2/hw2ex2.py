my_list = []
n = int(input('Сколько элементов будет в вашем списке? '))
for i in range(n):
    my_list.append(input('какой элемент вы хотите добавить? '))
print('Here is your list:', my_list)
if n % 2 == 0:
    for i in range(0, n, 2):
        a = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = a
else:
    new_list = my_list[:-1]
    for i in range(0, n-1, 2):
        a = new_list[i]
        new_list[i] = new_list[i+1]
        new_list[i+1] = a
    new_list.append(my_list[-1])
    my_list = new_list
print('Here is a modified list:', my_list)
