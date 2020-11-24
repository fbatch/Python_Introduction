# Working with my_file.txt
my_file = open("my_file.txt", "w", encoding='utf-8')
a = ' '
while len(a) > 0:
    a = input('Enter some text here: ')
    my_file.write(f'{a}\n')
my_file.close()
