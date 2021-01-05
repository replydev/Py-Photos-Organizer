import os
from locale import getdefaultlocale

def get_month_name(month_number,locale="en_US"):
    if month_number == "01":
        if locale == "it_IT":
            return "Gennaio"
        else:
            return "January"
    elif month_number == "02":
        if locale == "it_IT":
            return "Febbraio"
        else:
            return "February"
    elif month_number == "03":
        if locale == "it_IT":
            return "Marzo"
        else:
            return "March"
    elif month_number == "04":
        if locale == "it_IT":
            return "Aprile"
        else:
            return "April"
    elif month_number == "05":
        if locale == "it_IT":
            return "Maggio"
        else:
            return "May"
    elif month_number == "06":
        if locale == "it_IT":
            return "Giugno"
        else:
            return "June"
    elif month_number == "07":
        if locale == "it_IT":
            return "Luglio"
        else:
            return "July"
    elif month_number == "08":
        if locale == "it_IT":
            return "Agosto"
        else:
            return "August"
    elif month_number == "09":
        if locale == "it_IT":
            return "Settembre"
        else:
            return "September"
    elif month_number == "10":
        if locale == "it_IT":
            return "Ottobre"
        else:
            return "October"
    elif month_number == "11":
        if locale == "it_IT":
            return "Novembre"
        else:
            return "November"
    elif month_number == "12":
        if locale == "it_IT":
            return "Dicembre"
        else:
            return "December"
    else:
        if locale == "it_IT":
            return "Sconosciuto"
        else:
            return "Unknown"

def check_path(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        return None 
    elif not path.endswith("/"):
        return path + "/"
    else:
        return path

def get_filename(path):
    paths = path.split("/")
    return paths[len(paths) - 1]

def getLocale():
    return getdefaultlocale()[0]