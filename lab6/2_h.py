"""Delete a file at the specified path after checking for existence and access."""

import os

def delete_file(path):
    try:
        if os.path.exists(path):
            print(f"The path '{path}' exists.")
            if os.path.isfile(path):
                if os.access(path, os.W_OK):
                    os.remove(path)  # Delete the file
                    print(f"The file '{path}' has been deleted.")
                else:
                    print(f"Error: No write access to the file '{path}'.")
            else:
                print(f"Error: '{path}' is not a file.")
        else:
            print(f"Error: The path '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "example.txt"  
delete_file(file_path)