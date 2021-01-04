import os
from utils import get_filename,check_path

def restore(path):
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            os.rename(os.path.join(root,name),os.path.join(path,get_filename(name)))
        
def main():
    path = check_path(input("Insert folder: "))
    while path is None:
        print("Invalid folder")
        path = check_path(input("Insert folder: "))
    restore(path)


if __name__ == "__main__":
    main()

    