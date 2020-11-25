ex_2 = open('text_2.txt', 'r', encoding='utf-8')
content = ex_2.readlines()
# print(content)
num_lines = 0
num_words = 0
for line in content:
    line = line.split(' ')
    for word in line:
        num_words += 1
    print(f'There are {num_words} words in the {num_lines+1} line.')
    num_words = 0
    num_lines += 1
print(f'\nThere are {num_lines} lines in this file.')
ex_2.close()