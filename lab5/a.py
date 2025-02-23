import re

def match_pattern(string):

    pattern = r'^ab*$'     # Шаблон: начинается с 'a', за которой следует ноль или более 'b'
    if re.match(pattern, string):
        return True
    else:
        return False

test_strings = ["a", "ab", "abb", "ac", "b", "abc", "aab"]

for s in test_strings:
    if match_pattern(s):
        print(f"'{s}' Yes")
    else:
        print(f"'{s}' No")