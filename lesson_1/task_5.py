"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import chardet
import subprocess
import platform


def func_ping(a):
    for el in a:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        args = ['ping', param, '2', el]
        result = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in result.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))


WEB_1 = 'yandex.ru'
WEB_2 = 'youtube.com'

web_list = [WEB_1, WEB_2]

func_ping(web_list)
