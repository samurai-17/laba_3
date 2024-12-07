import unittest
from main import MainProgram


class TestCheckAll(unittest.TestCase):

    def setUp(self):
        """Setup данных"""
        self.program = MainProgram()
        self.valid_data = ["#aabbcc", "#123321", "#543901", "#aBcDeF"]
        self.invalid_data = ["#12345g", "#1234567", "######", ""]

    def test_check_the_string(self):
        """Тест функции проверки строки на валидных данных"""
        for i in self.valid_data:
            with self.subTest(i=i):
                self.assertEqual(self.program.check_the_string(text=i), f"Все найденные цвета: ['{i}']")

    def test_check_the_string2(self):
        """Тест функции проверки строки на не валидных данных"""
        for i in self.invalid_data:
            with self.subTest(i=i):
                self.assertEqual(self.program.check_the_string(text=i), "Цветов не найдено")

    def test_check_the_file(self):
        """Тест функции проверки строки на тестовом файле"""
        self.assertEqual(self.program.check_the_file(path="example.txt"),
                         "Все найденные цвета: ['#123456', '#aaafff', '#AAAFFF']")

    def test_check_the_url(self):
        """Тест функции проверки сайта на тестовом html-коде"""
        example_html = "<html><body>picker_wrapper{background:#f2f2f2}input:active{#1e90ff}</body></html>"
        self.assertEqual(self.program.check_the_string(text=example_html),
                         "Все найденные цвета: ['#f2f2f2', '#1e90ff']")


if __name__ == "__main__":
    unittest.main()
