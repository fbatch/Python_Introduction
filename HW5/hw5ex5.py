ex_5 = open('text_5.txt', 'w+', encoding='utf-8')
a = input('Enter some numbers: ')
ex_5.writelines(a)
b = 0
for el in a.split():
    if el.isdigit() == True:
        b += int(el)
content = ex_5.read()
print(f'Cумма чисел: {b}')
ex_5.writelines(f'\nCумма: {b}')
ex_5.close()
