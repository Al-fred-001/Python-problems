# This marks the beginning of a python script.

DATA: list[int] = [1,0]
TRUE_OR_FALSE : dict[int,bool] = {
    1: True,
    0: False
}

    
def is_valid(a:int, b:int):
    

    if ( a in DATA and b in DATA):
        return True
    else: 
        print("Please provide a valid input (1 or 0): ")
        print("--Try again--")
        return False


'''--Defining funcitons for logic gates--'''

# basic logic gates
def and_gate(a: int, b: int):
    if (a*b ==1):
        return 1
    else: 
        return 0

def or_gate(a: int, b: int):
    if ((a+b) != 0):
        return 1
    else:
        return 0

def not_gate(a: int):
    if (a == 1):
        return 0
    elif (a == 0):
        return 1

# universal logic gates
def nand_gate(a:int, b:int):
    result = not_gate(and_gate(a,b))
    return result

def nor_gate(a:int, b: int):
    result = not_gate(or_gate(a,b))
    return result


# exclusive gates
def xor_gate(a:int, b: int):
    if (a != b):
        return 1
    else:
        return 0

def xnor_gate(a:int, b: int):  #also called xand gate
    if (a==b):
        return 1
    else:
        return 0



# for testing purpose only
def main():
    #output for basic logic gates
    output_01 = and_gate(var_a, var_b)
    output_02 = or_gate(var_a, var_b)
    output_03 = not_gate(var_a)

    #output for universal logic gates
    output_04 = nand_gate(var_a, var_b)
    output_05 = nor_gate(var_a,var_b)

    #output for exclusive logic gates
    output_06 = xor_gate(var_a, var_b)
    output_07 = xnor_gate(var_a, var_b)
    print()
    print(f"""
    --The outputs are as follows--
    
    # Basic logic gates

    1) AND gate:{output_01}                  #{TRUE_OR_FALSE[output_01]}
    2) OR gate: {output_02}                  #{TRUE_OR_FALSE[output_02]}
    3) NOT gate: {output_03}                 #{TRUE_OR_FALSE[output_03]}

    # Universal logic gates
    
    1) NAND gate: {output_04}                #{TRUE_OR_FALSE[output_04]}
    2) NOR gate: {output_05}                 #{TRUE_OR_FALSE[output_05]}

    # Exclusive logic gates

    1) XOR gate: {output_06}                 #{TRUE_OR_FALSE[output_06]}
    2) XNOR or XAND gate: {output_07}        #{TRUE_OR_FALSE[output_07]}
    
    --Code execution completed--

    """)





if __name__ =="__main__":
    count =0
    while(count<=4):
        print()
        print("Please select the inputs:")
        print()
        print("1 denotes high or switched on condition. \n0 denotes low or switched off condition.")
        print()
        a = int(input("Enter the first digit (1 or 0): "))
        b = int(input("Enter the second digit(1 or 0): "))
        if (is_valid(a,b)):
            var_a = a
            var_b = b
            count +=5
            main()
        else:
            count+=1