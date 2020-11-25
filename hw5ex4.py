ex_4 = open('text_4.txt', 'r', encoding='utf-8')
content = ex_4.readlines()
for line in content: # Цикл для построчного вывода
    print(''.join(line), end='')
print('\n')
for line in content:
    line = line.split(' ')
    if line[0] == 'One':
        line[0] = 'Один'
    elif line[0] == 'Two':
        line[0] = 'Два'
    elif line[0] == 'Three':
        line[0] = 'Три'
    else:
        line[0] = 'Четыре'
    ex_4_1 = open('text_4_1.txt', 'a', encoding='utf-8')
    ex_4_1.writelines(' '.join(line))
    print(' '.join(line), end='')
ex_4_1.write('\n') # Если хотим запускать несколько раз
ex_4_1.close()
ex_4.close()
