#import cmath
#import re


def f(text):

    w = text.split()
    upper_count = 0
    lower_count = 0
    for word in w:
        for char in word:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
    return upper_count, lower_count
a = "lab6_b.txt"
b = "result6_b.txt"

try:
    with open(a, "r") as file:
        text = file.read()
    upper, lower = f(text)
    with open(b, "w") as file:
        file.write(f"upper letter: {upper}\n")
        file.write(f"lower letter: {lower}\n")

    print(f"my_result {b}")
except FileNotFoundError:
    print(f"error in f '{a}'.")
except Exception as e:
    print(f"error {e}")