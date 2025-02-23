def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    camel_str = parts[0] + ''.join(word.title() for word in parts[1:])# Первую часть оставляет без изменений, а остальные части преобразует, первую букву каждого слова делает заглавной, а остальные строчными
    
    return camel_str

snake_case_strings = ["snake_case_string", "hello_world", "python_programming", "convert_to_camel_case", "example_string"]
for s in snake_case_strings:
    print(f"Snake case: {s} -> Camel case: {snake_to_camel(s)}")