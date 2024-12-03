import re

def check_the_string(text):
    pattern = r"#[0-9a-fA-F]{6}\b"
    answer = re.findall(pattern, text)
    return answer

def check_the_file(path):
    file = open(path)
    s = file.read()
    return check_the_string(s)


t = 'example.txt'
print(check_the_file(t))