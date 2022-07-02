import os
from sys import argv
from datetime import date,timedelta,datetime
from dateutil.relativedelta import relativedelta as rd
from typing import List
from itertools import chain
import sys

SUB_LIST =  {
        "MUSIC":{"FREE":0,"PERSONAL":100,"PREMIUM":250 },
        "VIDEO":{"FREE":0,"PERSONAL":200,"PREMIUM":500 },
        "PODCAST":{"FREE":0,"PERSONAL":100,"PREMIUM":300 }
    }

TOPUP_LIST = {"FOUR_DEVICE":50,"TEN_DEVICE":100}

def calc_ren(self,mnths):
    return self.sub_start + rd(months=mnths)

def read_file(file_location):
    try:
        os.path.exists(file_location)
    except:
        raise Exception("File Not Found")
    else:
        print(f'Found File at {file_location}')
        pass

    f = open(file_location,"r")
    Lines = f.readlines()
    f.close()
    return Lines

def get_input_params(f_string):

    input_params = {}
    add_subs = []
    add_tops = []

    for line in f_string:
        curr_option = line.split(" ")[0].strip()
        #print("Line is {}".format(line))
        if curr_option == "START_SUBSCRIPTION":
            input_params[curr_option] = line.split(" ")[1]
        elif curr_option == "ADD_SUBSCRIPTION":
            add_subs.append([val for val in line.split(" ")[1:]])
            input_params[curr_option] = add_subs
        elif curr_option == "ADD_TOPUP":
            add_tops.append([val for val in line.split(" ")[1:]])
            input_params[curr_option] = add_tops
        elif curr_option == "PRINT_RENEWAL_DETAILS":
            input_params[curr_option] = "Yes"
        print(input_params)

    return input_params

def chk_dup_entry(lst:List) -> bool:
    l1=[]
    for i in lst:
        if i not in l1:
            l1.append(i)
        else:
            return True


def main(argv):
    '''
    This code is run as follows: 
        python geektrust.py "file1.txt"
    If the path is not entered, it will error out. 

    '''

    if len(argv) != 2:
        raise Exception("File path not entered.")
    else:
        file_loc = argv[1]
    
    input_string = read_file(file_loc) 

    if input_string:
        f_params = get_input_params(input_string)
    
    print(" ********** Printing output ********* \n ")
    
    for key in f_params:
        if key:
            print(f'{key} - {f_params[key]}')
    print(" \n ********* \n")

    
    if chk_dup_entry(f_params["ADD_SUBSCRIPTION"]):
        print(f'ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY\n')
        sys.exit()
    elif chk_dup_entry(f_params["ADD_TOPUP"]):
        print(f'ADD_TOPUP_FAILED DUPLICATE_TOPUP\n')
        sys.exit()





if __name__ == "__main__":
    main(argv)    
