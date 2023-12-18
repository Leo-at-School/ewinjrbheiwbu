from re import sub

derivative_output = 0
output_list = []
user_input = ""
user_funcs = []

print("Inut a function or type q to quit or c to continue")

while 1 == 1:
    while 1 == 1:
        user_input = input("> ")

        if user_input == "Q" or user_input == "q":
            print("> Exiting...")
            exit()

        elif user_input == "C" or user_input == "c":
            break

        else:
            user_funcs.append(user_input)

    if len(user_funcs) == 0:
        print("> Exiting: ")
        exit()

    for i in user_funcs:
        num_index = slice(0, i.find("x"))
        num_location = int(i[num_index])

        if "^" not in i or "^1" in i:  
            derivative_output = num_location

        else:
            exp_index = slice(i.find("^") + 1, -1)
            i += " "
            exp_location = int(i[exp_index])
            
            derivative_output = str(exp_location * num_location) + "x^" + str(exp_location - 1)
                    
    derivative_output = str(derivative_output)
    derivative_output = sub(" ", "", derivative_output)    
    
    print("> "+ derivative_output + " => " + i)
    output_list.append(derivative_output)

    print("> Input: " + str(user_funcs))
    print("> Ouput: " + str(output_list))
    
    derivative_output = 0
    output_list = []
    user_input = ""
    user_funcs = []
