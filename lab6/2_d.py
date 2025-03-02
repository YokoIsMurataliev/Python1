def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            line_count = sum(1 for line in file)
        print(f"The file '{filename}' contains {line_count} lines.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Указываешь файл для подсчета строк
filename = "Info.txt" 
count_lines(filename)


