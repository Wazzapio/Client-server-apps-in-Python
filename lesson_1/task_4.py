"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""


def func_to_bytes(a):
    print('----------------bytes----------------')
    for el in a:
        el_bytes = el.encode('utf-8')
        list_bytes.append(el_bytes)
        print(el_bytes)


def func_to_str(a):
    print('----------------str----------------')
    for el in a:
        el_str = el.decode('utf-8')
        print(el_str)


WORD_STR_1 = 'разработка'
WORD_STR_2 = 'администрирование'
WORD_STR_3 = 'protocol'
WORD_STR_4 = 'standard'
words_str = [WORD_STR_1, WORD_STR_2, WORD_STR_3, WORD_STR_4]
list_bytes = []

func_to_bytes(words_str)
func_to_str(list_bytes)
