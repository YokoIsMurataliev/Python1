import re

def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, text) # Используем re.findall для поиска всех совпадений в тексте
    return matches

text = """
This is a test_string with some_sequences like hello_world and python_programming.
"""
sequences = find_sequences(text) #вывод последовательности
print("Найденные последовательности:", sequences)