"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from main import get_html, write_json, get_data, URL

class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200 от сервера"""
        self.assertNotEqual(get_html(URL), None)

    def test_write_json(self):
        """Тест записи словаря в JSON"""
        self.assertEqual(write_json(get_data(get_html(URL)),os.getcwd()), True)

    def test_data_to_json(self):
        """Тест корректности данных при записи в словарь"""
        self.assertNotEqual(get_data(get_html(URL)), None)


if __name__ == '__main__':
    unittest.main()
