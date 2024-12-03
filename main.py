import re

def check_the_string(text):
    pattern = r'(^#[0-9a-fA-F]{6}$)'
    answer = re.findall(pattern, text)
    return answer

t = input()

print(check_the_string(t))