from re import sub

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

    print("-----")

    for i in user_funcs:
        i = str(i)

        if "x" not in i:
            derivative_output = "0"
        
        else:

            if i.find("x") == 0:
                if "^" not in i or "^1" in i:
                    num_index = slice(0, i.find("x"))
                    num_location = int(i[num_index])
                    derivative_output = num_location

                else:
                    exp_index = slice(i.find("^") + 1, -1)
                    
                    i += " "
                    
                    exp_location = int(i[exp_index])
                    derivative_output = str(exp_location) + "x^" + str(exp_location - 1)

            elif "^" not in i or "^1" in i:
                if i.find("x") == 0:
                    exp_index = slice(i.find("^") + 1, -1)
                    
                    i += " "
                    
                    exp_location = int(i[exp_index])
                    derivative_output = str(exp_location) + "x^" + str(exp_location - 1)

                else:  
                    num_index = slice(0, i.find("x"))
                    num_location = int(i[num_index])
                    derivative_output = num_location

            else:
                num_index = slice(0, i.find("x"))
                num_location = int(i[num_index])
                exp_index = slice(i.find("^") + 1, -1)
                
                i += " "

                exp_location = int(i[exp_index])
                derivative_output = str(exp_location * num_location) + "x^" + str(exp_location - 1)
                        
        derivative_output = str(derivative_output)
        if "^1" in derivative_output:
            derivative_output = derivative_output[:-2]
        derivative_output = sub(" ", " ", derivative_output)
            
        print("> "+ i + " => " + derivative_output)
        output_list.append(derivative_output)

    print("-----")
    print("> Input: " + str(user_funcs))
    print("> Ouput: " + str(output_list))
    
    output_list = []
    user_input = ""
    user_funcs = []
