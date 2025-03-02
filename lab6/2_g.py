"""Copy the contents of a source file to a destination file."""

def copy_file(source_file, destination_file):
    try:
        with open(source_file, "r", encoding="utf-8") as src:
            with open(destination_file, "w", encoding="utf-8") as dest:
                dest.write(src.read())  # Копирование 
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = "source.txt"  
destination_file = "destination.txt"  
copy_file(source_file, destination_file)