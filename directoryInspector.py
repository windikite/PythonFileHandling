import os

def list_directory_contents(path):
    try:
        valid_path = str(path)
        dir = os.listdir(valid_path)
    except FileNotFoundError:
        print("FileNotFoundError! Please input a valid path.")
    except PermissionError:
        print("PermissionError! This program lacks permission to read or write to that path.")
    except Exception as e:
        print("Error!", e)
    else:
        print(dir)

path = str(input("Please enter directory path: "))
list_directory_contents(path)