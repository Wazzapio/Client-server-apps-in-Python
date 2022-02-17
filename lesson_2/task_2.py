"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(lst):
    params = {'товар (item)': '', 'количество (quantity)': '', 'цена (price)': '', 'покупатель (buyer)': '',
              'дата (date)': '', }
    pos = 0
    for par in params:
        params[par] = lst[pos]
        pos += 1
    with open('orders.json') as f_n:
        f_n_content = f_n.read()
        objs = json.loads(f_n_content)
        for i in objs:
            if objs[i] == []:
                objs[i].append(params)
            else:
                objs[i] = []
                objs[i].append(params)
        print(objs)
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(objs, f_n, indent=4, ensure_ascii=False)
    with open('orders.json', encoding='utf-8') as f_n:
        f_n_content = f_n.read()
        print(f_n_content)


values = ['Шарф', 1, 500, 'Mr.X', '10.02.2022']

write_order_to_json(values)
