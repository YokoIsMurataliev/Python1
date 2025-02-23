import re

def match_string(s):
    pattern = r'ab{2,3}'
    
    #проверка, соответствует ли строка шаблону
    if re.match(pattern, s):
        return True
    else:
        return False

test_strings = [
    "abb",    # Соответствует (a и 2 b)
    "abbb",   # Соответствует (a и 3 b)
    "ab",     # Не соответствует (a и только 1 b)
    "abbbb",  # Не соответствует (a и 4 b)
    "aabbb",  # Не соответствует (начинается с aa)
    "xabb",   # Не соответствует (начинается с x)
    "abx",    # Не соответствует (содержит x после b)
]

for s in test_strings:
    print(f"'{s}': {match_string(s)}")