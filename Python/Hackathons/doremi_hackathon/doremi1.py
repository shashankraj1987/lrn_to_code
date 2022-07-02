# Doremi Hackathon

import os
import sys
from datetime import date, datetime

menu_options = {
    1:" START_SUBSCRIPTION (DD-MM-YYYY) ",
    2:" ADD_SUBSCRIPTION (SUBSCRIPTION_CATEGORY) (PLAN_NAME) ",
    3:" ADD_TOPUP (TOP_UP_NAME) (NO_OF_MONTHS) ",
    4:" PRINT_RENEWAL_DETAILS ",
    5:" man pages ",
    6:" quit "
 }

def main():
    if os.name == 'posix' or os.name == 'darwin':
        os.system('clear')
    else:
        os.system('cls')
    
    # Give user the choices to input the options
    print("\n")
    print(f"*"*101)
    print(f"*"*47,"Hello","*"*47) 
    print(f"*"*101,'\n')

    print(f'Enter One of the options in the Below Input:\n')

    option = ""
    valid_date = ""
    date_part = ""

    while option != "quit":
        print_menu()
        option = input("\nEnter Your choice <Case Sensitive>:")
        if option == "START_SUBSCRIPTION":
            date_part = option.split()[1]
        elif option.strip().startswith("man"):
            pass
        elif option.startswith("ADD_"):
            pass
        elif option == "PRINT_RENEWAL_DETAILS":
            pass
        elif option == "quit":
            quit()

    valid_date = convert_date(date_part)
    if valid_date:
        print(f'Date is {datetime.strptime(date_part)}')
    else:
        print("Invalid Date")
        sys.exit()

def print_menu() -> None:
    for x in menu_options.keys():
        print(f'{x}){menu_options[x]}')

def convert_date(date_obj:datetime)-> int:
    format = "%d-%m-%Y"
    try:
        datetime.strptime(date_obj,format)
    except:
        return -1
    else:
        return 0


if __name__ == "__main__":
    main()

