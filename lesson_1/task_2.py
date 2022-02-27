"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""


def func(a):
    for el in a:
        el = eval(f'B"{el}"')
        print('-----------------')
        print(type(el))
        print(el)
        print(len(el))


WORD_STR_1 = 'class'
WORD_STR_2 = 'function'
WORD_STR_3 = 'method'
words_str = [WORD_STR_1, WORD_STR_2, WORD_STR_3]
B = b''

func(words_str)
