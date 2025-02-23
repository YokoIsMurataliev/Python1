import re

def insert_spaces(text):

    result = re.sub(r'(?<!^)([A-Z])', r' \1', text)# Использует регулярное выражение для поиска заглавных букв и вставки пробелов
    return result

text = "HelloWorldMyNameIsIskander"
modified_text = insert_spaces(text)
print("Оригинальная строка:", text)
print("Изменённая строка:", modified_text)