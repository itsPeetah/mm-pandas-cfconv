import sys
from functions import render_xlsx, process_xlsx
from datetime import datetime
from os import system
current_year = datetime.now().year

default_fileout_names = [
    f"~/Desktop/cashflow_{current_year}_v1.xlsx",
    f"~/Desktop/cashflow_{current_year}_v2.xlsx"
]

months = {
 1:"Gennaio", 2:"Febbraio", 3:"Marzo",
 4:"Aprile", 5:"Maggio", 6:"Giugno",
 7:"Luglio", 8:"Agosto", 9:"Settembre",
 10:"Ottobre", 11:"Novembre", 12:"Dicembre"   
}

def main():
    while True:
        src = input("Please select input file: ")[1:-1]
        try:
            df1, df2 = process_xlsx(src,current_year, months)
        except:
            print("Something went wrong...")
            continue
        system("clear")
        print("Leave the file name empty for default save location (~/Desktop/)")
        fn1 = input("Save converted file (v1) as: ")
        fn2 = input("Save converted file (v2) as: ")
        if len(fn1) < 1: fn1 = default_fileout_names[0]
        else: fn1 += ".xlsx"
        if len(fn2) < 1: fn2 = default_fileout_names[1]
        else: fn2 += ".xlsx"
        try:
            render_xlsx(df1, fn1)
            render_xlsx(df2, fn2)
        except:
            print("Something went wrong...")
            continue
        else:
            break


if __name__ == "__main__":
    main()