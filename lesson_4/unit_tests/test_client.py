import unittest
import os.path
import sys

from client import create_presence, process_ans
from common.variables import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, RESPONSE, ERROR

sys.path.append(os.path.join(os.getcwd(), '..'))


class TestCreatePresence(unittest.TestCase):  # тест формирования presence-сообщения

    def test_create_presence(self):
        # Ошибка если некорректный запрос
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_without_action(self):
        # Ошибка если нет ACTION
        test = create_presence({TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_without_time(self):
        # Ошибка если нет TIME
        test = create_presence({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}})
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_without_user(self):
        # Ошибка если нет USER
        test = create_presence({ACTION: PRESENCE, TIME: 1.1})
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_without_account_name(self):
        # Ошибка если нет ACCOUNT_NAME
        test = create_presence({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: ''}})
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_empty(self):
        # Ошибка если нет ACCOUNT_NAME
        test = create_presence('')
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})


class TestProcessAns(unittest.TestCase):  # тест разбора сообщения от сервера

    def test_process_ans_200(self):
        # Ошибка если некорректное сообщение
        test = process_ans({RESPONSE: 200})
        self.assertEqual(test, '200 : OK')

    def test_process_ans_400(self):
        # Ошибка если некорректное сообщение
        test = process_ans({RESPONSE: 400, ERROR: 'Bad Request'})
        self.assertEqual(test, f'400 : Bad Request')

    def test_process_ans_without_message(self):
        # Ошибка если нет сообщения
        self.assertRaises(ValueError, process_ans, f'400 : Bad Request')


if __name__ == '__main__':
    unittest.main()
