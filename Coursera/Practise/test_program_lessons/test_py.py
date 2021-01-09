# импортируем библиотеку тестирования и сам модуль,который мы будем тестировать
# для внесения информации перед каждым тестом используем setUp()
import unittest
import calc


class CalcTest(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 1

    def tearDown(self) -> None:
        print('Test is end')

    def test_add(self):
        self.assertEqual(calc.add(self.name, 8), 9)

    def test_mul(self):
        self.assertEqual(calc.div(10, 5), 2)

    def test_div(self):
        self.assertEqual(calc.mul(6, 3), 18)

    def test_sub(self):
        self.assertEqual(calc.sub(7, 3), 4)