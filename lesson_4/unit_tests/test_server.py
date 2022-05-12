import unittest
import os.path
import sys

from common.variables import RESPONSE, ERROR, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME
from server import process_client_message

sys.path.append(os.path.join(os.getcwd(), '..'))


class TestProcessClientMessage(unittest.TestCase):  # тест обработчика сообщений от клиента

    def test_process_client_message_200(self):
        # Ошибка если некорректный запрос
        test = process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, {RESPONSE: 200})

    def test_process_client_message_without_action(self):
        # Ошибка если нет ACTION
        test = process_client_message({TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_client_message_without_time(self):
        # Ошибка если нет TIME
        test = process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_client_message_without_user(self):
        # Ошибка если нет USER
        test = process_client_message({ACTION: PRESENCE, TIME: 1.1})
        self.assertEqual(test, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_client_message_without_account_name(self):
        # Ошибка если нет ACCOUNT_NAME
        test = process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: ''}})
        self.assertEqual(test, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_client_message_empty(self):
        # Ошибка если нет сообщения
        test = process_client_message('')
        self.assertEqual(test, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_client_message_not_200(self):
        # Ошибка если корректное сообщение возвращает RESPONSE: 400
        test = process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertNotEqual(test, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_client_message_empty_not_400(self):
        # Ошибка если пустое сообщение возвращает RESPONSE: 200
        test = process_client_message('')
        self.assertNotEqual(test, {RESPONSE: 200})


if __name__ == '__main__':
    unittest.main()
