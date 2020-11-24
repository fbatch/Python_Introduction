# ДОПИСАТЬ ПЕРЕВОД В JSON!!!

ex_7 = open('text_7.txt', 'r', encoding='utf-8')
content = ex_7.readlines()
b = 0
c = 0
my_dict1 = {}
my_dict2 = {}
lst = [my_dict1, my_dict2]
for line in content:
    line = line.split()
    a = int(line[2]) - int(line[3])
    my_dict1[str(line[0])] = a
    if a > 0:
        b += a
        c += 1
average_profit = b / c
my_dict2['average_profit'] = "{:.0f}".format(average_profit)
print(lst)
ex_7.close()
