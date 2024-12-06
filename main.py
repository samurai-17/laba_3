import re
import requests


class MainProgram:

    def check_the_string(self, text):
        """Функция проверки строчки"""
        pattern = r"#[0-9a-fA-F]{6}\b"
        answer = re.findall(pattern, text)
        if not answer:
            return f"Цветов не найдено"
        return f"Все найденные цвета: {answer}"

    def check_the_file(self, path):
        """Функция проверки файла"""
        try:
            with open(path, encoding="utf-8") as file:
                s = file.read()
                return self.check_the_string(s)
        except Exception as e:
            return f"Ошибка открытия файла: {e}"

    def check_the_url(self, url):
        """Функция проверки сайта"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return self.check_the_string(response.text)
        except Exception as e:
            return f"Ошибка чтения страницы: {e}"

    def main_window(self):
        """Запуск программы"""
        t = 1
        while t != 0:
            print("Что вы хотите проверить?")
            print("1 - строку", "\n2 - файл", "\n3 - url", "\n0 - Выход")
            t = int(input())
            if t == 1:
                print("Введите строку")
                ex = str(input())
                print(self.check_the_string(ex))
            elif t == 2:
                print("Введите путь к файлу")
                ex = str(input())
                print(self.check_the_file(ex))
            elif t == 3:
                print("Введите url")
                ex = str(input())
                print(self.check_the_url(ex))


solution = MainProgram()
solution.main_window()
