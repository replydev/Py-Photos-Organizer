from organizer import organize
from renamer import rename
from utils import check_path

def main():
    
    path = check_path(input("Path: "))

    if path is None:
        print("Invalid path.")
        return
    rename(path)
    organize(path)
    print("Done.")

if __name__ == "__main__":
    main()
    
    