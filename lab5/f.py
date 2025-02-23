import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text) # замена всех совпадений на двоеточие
    
    return result

text = "Hello world, it is me Mario, who are you?"

modified_text = replace_with_colon(text) # Замена пробелов, запятых и точек на двоеточия

print("Оригинальный текст:", text)
print("Изменённый текст:", modified_text)