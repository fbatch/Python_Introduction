# Exercise 6 a = chr(ord('A') - 22)
def title_self_made():
    word = input('Введите ваше слово: ')
    word_modified = chr(ord(word[0]) - 32) + word[1:]
    print(word_modified)

def title_pro_self_made():
    a = []
    words = input('Введите строку из слов: ').split()
    for word in words:
        for letter in word:
            if ord(letter) not in range(97, 122):
                word_1 = word
                break
            else:
                word_1 = chr(ord(word[0]) - 32) + word[1:]
        a.append(word_1)
    print(' '.join(a))

title_pro_self_made()