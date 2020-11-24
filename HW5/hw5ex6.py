ex_6 = open('text_6.txt', 'r', encoding='utf-8')
content = ex_6.readlines()
a = 0
my_dict = {}
for line in content:
    for el in line.split():
        if el[0].isdigit() == True and el[1].isdigit() == True:
            if el[:2].isdigit() == True:
                a += int(el[:2])
#           print(a)
        else:
            if el[0].isdigit() == True:
                a += int(el[0])
#           print(a)
    my_dict[str(line.split()[0])] = a
#   print(f'{line.split()[0]} {a}')
    a = 0
print(my_dict)