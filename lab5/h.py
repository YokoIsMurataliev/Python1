import re

def split_at_uppercase(text):

    parts = re.split(r'(?=[A-Z])', text) #re.split для разделения строки перед заглавными буквами
    result = ' '.join(parts) # Соединяет части с пробелом для удобства чтения
    
    return result

text = "HelloWorldMyNameIsIskander"
split_text = split_at_uppercase(text)
print("Original string:", text)
print("Split string:", split_text)