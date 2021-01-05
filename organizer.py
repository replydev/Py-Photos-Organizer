import os
import time
from utils import get_month_name,check_path,get_filename

def get_year(path):
    return get_filename(path)[0:4] + "/"

def get_month(path,locale):
    return get_month_name(get_filename(path)[4:6],locale) + "/"

def organize(path,locale):
    filenames = os.listdir(path)
    years = []
    for f in filenames:
        filepath = os.path.join(path, f)
        if not os.path.isfile(filepath):
            continue
        yearpath = os.path.join(path, get_year(filepath))
        if yearpath not in years:
            years.append(yearpath)
            if not os.path.exists(yearpath):
                os.mkdir(yearpath)
        os.rename(filepath,os.path.join(yearpath, f))
    for year in years:
        organize_month(year,locale)
    
def organize_month(path,locale):
    filenames = os.listdir(path)
    for f in filenames:
        filepath = path + f
        if not os.path.isfile(filepath):
            continue
        monthpath = path + get_month(filepath,locale)
        if not os.path.exists(monthpath):
            os.mkdir(monthpath)
        os.rename(filepath,monthpath + f)

def main():
    path = check_path(input("Insert folder: "))
    while path is None:
        print("Invalid folder")
        path = check_path(input("Insert folder: "))
    organize(path,"it")

if __name__ == "__main__":
    main()
        