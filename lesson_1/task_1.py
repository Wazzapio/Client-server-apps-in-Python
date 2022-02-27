"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
"""


def func(a):
    for el in a:
        print(type(el))
        print(el)


WORD_STR_1 = 'разработка'
WORD_STR_2 = 'сокет'
WORD_STR_3 = 'декоратор'
words_str = [WORD_STR_1, WORD_STR_2, WORD_STR_3]

WORD_UNICODE_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
WORD_UNICODE_2 = '\u0441\u043e\u043a\u0435\u0442'
WORD_UNICODE_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
words_unicode = [WORD_UNICODE_1, WORD_UNICODE_2, WORD_UNICODE_3]

print('--------------str--------------')
func(words_str)
print('--------------unicode--------------')
func(words_unicode)
