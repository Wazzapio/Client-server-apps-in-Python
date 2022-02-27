"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect


def func(a):
    file = open('test_file.txt', 'w')
    for el in a:
        file.write(el + '\n')
    file.close()
    with open('test_file.txt', 'rb') as f:
        content = f.read()
    encoding = detect(content)['encoding']
    print('encoding: ', encoding)
    with open('test_file.txt', encoding=encoding) as f_n:
        for el_str in f_n:
            print(el_str, end='')
        print()


WORD_STR_1 = 'сетевое программирование'
WORD_STR_2 = 'сокет'
WORD_STR_3 = 'декоратор'
words_str = [WORD_STR_1, WORD_STR_2, WORD_STR_3]

func(words_str)
