"""Generate 26 text files named A.txt, B.txt, ..., Z.txt."""

import os

def generate_files():

    try:
        
        if not os.path.exists("alphabet_files"): # Создаю каталог для хранения файлов
            os.makedirs("alphabet_files")
        
        for letter in range(ord('A'), ord('Z') + 1):
            filename = f"alphabet_files/{chr(letter)}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"This is the content of {chr(letter)}.txt\n")
        
        print("26 text files (A.txt to Z.txt) have been generated in the 'alphabet_files' directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_files()