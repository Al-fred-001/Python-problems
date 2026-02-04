# This marks the beginning of a python scirpt. 


def calc_factorial(n:int) -> int:
    count : int =1
    result: int = 1

    while(count<=n):
        result *=count
        count +=1
    return result


def exponent_to(a, b):
    return a**b


def sine_of_x(n):

    # radian_value: float = round(conv_to_radian(n),4)
    result =0
    numerator =0
    denominator = 0

    for i in range(1,26):
        numerator = exponent_to(-1,i-1)*exponent_to(n, 2*i-1)
        denominator = calc_factorial(2*i-1)
        result += numerator/denominator

    round(result,4)
    print(result)
    return result


input_in_radian = float(input("Enter the value of x (in degrees): "))
sine_of_x(input_in_radian)

