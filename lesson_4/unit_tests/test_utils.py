import json
import unittest
import os.path
import sys

from common.utils import send_message, get_message
from common.variables import ENCODING, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME

sys.path.append(os.path.join(os.getcwd(), '..'))


class TestSocket:
    #  Тестовый класс для создания словаря который будет прогоняться
    #  через тестовые функции
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        #  Тестовая функция отправки. Корректно кодирует сообщение, сохраняет, то что должно быть
        #  отправлено в сокет.
        #  message_to_send - то что отправляем в сокет.
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):
        #  Получаем данные из сокета
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    #  Класс для тестов функций utils.py
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {
            ACCOUNT_NAME: 'test_name'
        }
    }

    def test_send_message_true(self):
        #  Тестовая функция отправки корректного сообщения
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_not_dict(self):
        #  Тестовая функция отправки НЕкорректного сообщения (передается НЕ словарь)
        test_socket = TestSocket(self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, 'wrong massage')

    def test_get_message(self):
        #  Тестовая функция приема корректного сообщения
        test_socket = TestSocket(self.test_dict_send)
        self.assertEqual(get_message(test_socket), self.test_dict_send)

    def test_get_message_empty(self):
        #  Тестовая функция приема пустого сообщения
        self.assertRaises(AttributeError, get_message, '')


if __name__ == '__main__':
    unittest.main()
