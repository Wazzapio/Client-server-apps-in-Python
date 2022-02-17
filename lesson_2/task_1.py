"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import re

from chardet import detect


def get_data(files_txt):
    params = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    main_values_file_1 = []
    main_values_file_2 = []
    main_values_file_3 = []

    main_values = [main_values_file_1, main_values_file_2, main_values_file_3]
    main_data = []

    for file in files_txt:
        os_prod_list = []
        os_name_list = []
        os_code_list = []
        os_type_list = []

        values = [os_prod_list, os_name_list, os_code_list, os_type_list]
        print(f'\n----------------------------------{file}----------------------------------')
        pos = 0
        while pos != len(params):
            with open(file, 'rb') as f:
                content = f.read()
            encoding = detect(content)['encoding']
            with open(file, encoding=encoding) as f_n:
                for el_str in f_n:
                    if re.search(params[pos], el_str):
                        print(el_str, end='')
                        els_split = re.split(r':|\s+', el_str)
                        for el in els_split:
                            if not el in params[pos] and not '':
                                values[pos].append(el)
                        delimiter = ' '
                        values[pos] = delimiter.join(values[pos])
                        pos += 1
                        break
        for i in range(len(values)):
            main_values[files_txt.index(file)].append(values[i])
        print(values)
        print(f'----------------------------------{file}----------------------------------\n')
    main_data.append(params)
    for lst in main_values:
        main_data.append(lst)
    return main_data


def write_to_csv(link_file):
    main_data = get_data(files)

    with open(link_file, 'w') as f_n:
        f_n_writer = csv.writer(f_n, lineterminator='\n')
        f_n_writer.writerows(main_data)

    with open(link_file) as f_n:
        print(f_n.read())


files = ['info_1.txt', 'info_2.txt', 'info_3.txt']

write_to_csv('main_data.csv')
