# This marks the beginning of a python script.

def calc_factorial(n: int) -> int:
    counter: int =1
    result: int =1
    while(counter<=n and n>0):
        result *=counter
        counter +=1
    return result
        
def calc_permutation(n:int, r: int) -> int:
    numerator: int = calc_factorial(n)
    denominator: int = calc_factorial(n-r)
    result: int = int(numerator/denominator)
    return result
    
def calc_combination (n: int, r: int) -> int:
    numerator:int = calc_factorial(n)
    denominator: int = calc_factorial(n-r)*calc_factorial(r)
    result = int(numerator/denominator)
    return result
    


def main()->None:
    print()
    print("--Initializing--")
    print()
    user_input_n: int = int(input("Enter the value for n: "))
    user_input_r: int = int(input("Enter the value for r: "))

    result_per = calc_permutation(user_input_n, user_input_r)
    result_com = calc_combination(user_input_n, user_input_r)
    print()
    print(f"The required permutation : P({user_input_n},{user_input_r}) = {result_per}")
    print(f"The required combination: C({user_input_n},{user_input_r}) = {result_com}")
    print()
    print("--Code execution completed--\n")

# for testing purposes only. 
if __name__ =="__main__":
    main()