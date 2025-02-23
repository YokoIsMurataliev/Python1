import re

def camel_to_snake(camel_str):

    snake_str = re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower() # Использует регулярное выражение для вставки подчёркиваний перед заглавными буквами и преобразуем строку в нижний регистр
    return snake_str
camel_case_strings = ["KazakhstanRepublic", "RussiaFederation", " ", "HelloWorld"]
for s in camel_case_strings:
    print(f"Camel case: {s} -> Snake case: {camel_to_snake(s)}")