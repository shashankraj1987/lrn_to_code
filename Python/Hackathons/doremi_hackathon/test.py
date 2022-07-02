file_location = "sample_input/input2.txt"

f = open(file_location,"r")
Lines = f.readlines()
f.close()

input_params = {}
sub_list = {}
topup_list = {}

for line in Lines:
    curr_option = line.split(" ")[0].strip()
    if curr_option == "START_SUBSCRIPTION":
        input_params[curr_option] = line.split(" ")[1]
    elif curr_option in ["ADD_SUBSCRIPTION","ADD_TOPUP"]:
        sub_type = line.split(" ")[1]
        sub_value = line.split(" ")[2]
        # print(curr_option," ",sub_type," ",sub_value)
        
        if curr_option == "ADD_SUBSCRIPTION":
            sub_list[sub_type] = sub_value
            input_params[curr_option] = sub_list
        else:
            topup_list[sub_type]= sub_value
            input_params[curr_option] = topup_list
    elif curr_option == "PRINT_RENEWAL_DETAILS":
        input_params[curr_option] = True

print("\n","*"*50)

for key in input_params:
    print(key, "--- ", input_params[key])