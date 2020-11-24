# Working with text_1.txt
my_file = open("text_1.txt", "w", encoding='utf-8')
a = ' '
while len(a) > 0:
    a = input('Enter some text here: ')
    my_file.write(f'{a}\n')
my_file.close()
