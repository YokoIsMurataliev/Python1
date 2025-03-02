#не получилось потому что не правильны пути к файлу, да код взять из прошлых задач и создан по ним же

import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")

        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print(f"Directory portion: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = "Info.txt" # Проверка путей
check_path(path)