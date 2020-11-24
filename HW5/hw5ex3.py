ex_3 = open('text_3.txt', 'r', encoding='utf-8')
content = ex_3.readlines()
# print(content)
lst = []
total_salary = 0
for line in content:
    line = line.split(' ')
    if float(line[1]) < 20000:
        lst.append(line[0])
    total_salary += float(line[1])
average_salary = "{:.0f}".format(total_salary / len(content))
print(f'{average_salary} - средняя зарплата.')
print(f"{', '.join(lst)} получают меньше 20000 в месяц.")
ex_3.close()