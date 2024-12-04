import unittest
import main


class TestCheckAll(unittest.TestCase):

    def setUp(self):
        self.valid_data = ["#aabbcc", "#123321", "#543901", "#aBcDeF"]
        self.invalid_data = ["#12345g", "#1234567", "######", ""]

    def test_check_the_string(self):
        for i in self.valid_data:
            with self.subTest(i=i):
                self.assertEqual(main.check_the_string(i), f"Все найденные цвета: ['{i}']")

    def test_check_the_string2(self):
        for i in self.invalid_data:
            with self.subTest(i=i):
                self.assertEqual(main.check_the_string(i), "Цветов не найдено")

    def test_check_the_file(self):
        self.assertEqual(main.check_the_file("example.txt"), "Все найденные цвета: ['#123456', '#aaafff', '#AAAFFF']")

    def test_check_the_url(self):
        example_html = "<html><body>picker_wrapper{background:#f2f2f2}input:active{#1e90ff}</body></html>"
        self.assertEqual(main.check_the_string(example_html), "Все найденные цвета: ['#f2f2f2', '#1e90ff']")