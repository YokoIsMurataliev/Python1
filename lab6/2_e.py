"""Write a list to a file, with each element on a new line."""

def write_list_to_file(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for item in data:
                file.write(f"{item}\n")  # Пишу каждый элемент за которым следует новая строка
        print(f"The list has been written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

filename = "output.txt"  
write_list_to_file(filename, data)