import re

def find_sequences(text):
    pattern = r'\b[A-Z][a-z]+\b'
    matches = re.findall(pattern, text)
    return matches

text = """
This is a Test string with Some Sequences like Python, Regex, and MachineLearning.
"""
sequences = find_sequences(text)
print("Найденные последовательности:", sequences)