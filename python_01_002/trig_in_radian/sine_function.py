# This marks the beginning of a python script. 

#calculates the factorial
def calc_factorial(n:int) -> int:
    count : int =1
    result: int = 1

    while(count<=n):
        result *=count
        count +=1
    return result

# converts degrees to radian
def degree_to_radian(n):
    _PI = 3.141592653589793238
    return (n*_PI)/180

# raises power of a to b.
def exponent_to(a, b):
    return a**b

#the main logic of the function. (sinx)
def sine_of_x(n:int):

    radian_value: float = round(degree_to_radian(n),4)
    result: float =0
    numerator: float =0
    denominator: int = 0

    for i in range(1,70):
        numerator = exponent_to(-1,i-1)*exponent_to(radian_value, 2*i-1)
        denominator = calc_factorial(2*i-1)
        result += numerator/denominator

    # print(f"{round(result,4)}") #can be used to round decimals to 4 places
    return round(result, 4) # can use return round(result, x) to round result to x places


def main():
    input_degrees = int(input("Enter the value of x (in degrees): "))
    sin_x = sine_of_x(input_degrees)
    print(sin_x) #prints the return statemeent of the function call. 



#only executes thsi line if the file itself is being run. 
# Else if it's being used as a module it does not get executed.

if __name__ =="__main__":
    main()