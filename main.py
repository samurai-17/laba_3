import re
import requests


def check_the_string(text):
    pattern = r"#[0-9a-fA-F]{6}\b"
    answer = re.findall(pattern, text)
    if not answer:
        return f"Цветов не найдено"
    return f"Все найденные цвета: {answer}"


def check_the_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            s = file.read()
            return check_the_string(s)
    except Exception as e:
        return f"Ошибка открытия файла: {e}"


def check_the_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return check_the_string(response.text)
    except Exception as e:
        return f"Ошибка чтения страницы: {e}"


