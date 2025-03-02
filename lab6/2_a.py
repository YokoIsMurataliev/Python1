import os

def list_directories(path):
    print("Directories:") # Считает все каталоги по указанному пути
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

def list_files(path):
    print("Files:") # Cписок всех файлов по указанному пути.
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all(path): #Cписок всех каталогов и файлов.
    print("All directories and files:")
    for entry in os.listdir(path):
        print(entry)

path = "."
list_directories(path) # Список каталогов, файлов и всех записей
print() 
list_files(path)
print()  
list_all(path)