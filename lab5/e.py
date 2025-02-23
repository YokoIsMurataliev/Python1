import re

def match_string(s):

    pattern = r'^a.*b$'
    if re.match(pattern, s): #проверка, соответствует ли строка шаблону 
        return True
    else:
        return False
    
test_strings = [
    "acb", "a123b", "ab", "aXYZb", "a_b", "abc", "bca", "a", "b", "axyzb123",     
]

for s in test_strings:
    print(f"'{s}': {match_string(s)}")