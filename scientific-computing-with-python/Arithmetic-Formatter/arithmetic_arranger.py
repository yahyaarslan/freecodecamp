def arithmetic_arranger(input):

    length = len(input)
    # No more than 5 problems.
    if length > 5:
        error_handler("Error: Too many problems.")

    # Addition and substractions only.
    # Max of four digits.
    add_or_sub = []
    for index in range(0, length, 1):
        if (input[index].find('+')) >= 1:
            #print("Addition for: ", input[index])
            add_or_sub.append(0)
        elif (input[index].find('-')) >= 1:
            #print ("Subtraction for: ", input[index])
            add_or_sub.append(1)
        else:
            print(input[index])
            error_handler("Error: Operator must be '+' or '-'.")
    #print("List:", add_or_sub)

    # Only contain digits.
    temp = []
    for index in range(0, length, 1):
        if add_or_sub[index] == 0: # addition.
            temp = input[index].split('+')
            for index in range(0, len(temp), 1):
                try:
                    float(temp[index])
                except:
                    error_handler("Error: Numbers must only contain digits.")
                if len(temp[index]) > 4:
                    error_handler("Error: Numbers cannot be more than four digits.")

        if add_or_sub[index] == 1: # subtraction.
            temp = input[index].split('-')
            for index in range(0, len(temp), 1):
                try:
                    float(temp[index])
                except:
                    error_handler("Error: Numbers must only contain digits.")
                if len(temp[index]) > 4:
                    error_handler("Error: Numbers cannot be more than four digits.")

    
    # Return
    print(input)
    temp = []
    upper = []
    lower = []
    lengths = []
    for index in range(0, length, 1):
        temp = input[index]
        if add_or_sub[index] == 0:
            temp = temp.split('+')
            upper.append(temp[0])
            lower.append(temp[1])
            lengths.append(len(upper))
            lengths.append(len(lower))
        elif add_or_sub[index] == 1:
            temp = temp.split('-')
            upper.append(temp[0])
            lower.append(temp[1])
            lengths.append(len(upper))
            lengths.append(len(lower))
        #test = float(input[index])
        #print("Test", [index], test)
    print("Lengths:", lengths)
    print("Upper:", upper)
    print("Lower: ", lower)
   #print("Result:", input)

    temp = 0
    for index in range(0, length, 1):
        if len(upper[index]) > len(lower[index]):
            temp = len(upper[index])
        else:
            temp = len(lower[index])
        print(temp)
        for index in range(0, temp, 1):
            print(" ", end = '')
    print("test")


def error_handler(desription):
    print(desription)
    exit(1)
    
