def is_palindrome(s):
    cleaned_string = s.lower().replace(" ", "")
    return cleaned_string == cleaned_string[::-1]

input_file = "example_lab6_c.txt"
output_file = "result6_c.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines() 

    with open(output_file, "w", encoding="utf-8") as file:
        for line in lines:
            line = line.strip()
            if line:
                if is_palindrome(line):
                    file.write(f'"{line}" — это палиндром.\n')
                else:
                    file.write(f'"{line}" — это не палиндром.\n')

    print(f"{output_file}")
except FileNotFoundError:
    print(f"Ошибка: файл {input_file} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")