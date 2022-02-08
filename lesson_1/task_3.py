"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""


def func(a):
    for el in a:
        try:
            eval(f'B"{el}"')
        except SyntaxError:
            print(f'Слово "{el}" невозможно записать в байтовом типе.')


WORD_STR_1 = 'attribute'
WORD_STR_2 = 'класс'
WORD_STR_3 = 'функция'
WORD_STR_4 = 'type'
words_str = [WORD_STR_1, WORD_STR_2, WORD_STR_3, WORD_STR_4]
B = b''

func(words_str)
