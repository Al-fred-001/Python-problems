# This marks the beginning of a python script. 
from sine_function import calc_factorial, exponent_to, degree_to_radian

def cosine_of_x(n):

    radian_value = degree_to_radian(n)
    result = 1
    numerator = 0
    denominaor = 0

    for i in range(1, 70):
        numerator = exponent_to(-1,i)*exponent_to(radian_value, 2*i)
        denominaor = calc_factorial(2*i)
        result += numerator/denominaor

    # print(round(result,4))
    return round(result, 4)

def main():
    input_degrees = float(input("Enter value of x (in degrees): "))
    cosine_of_x(input_degrees)

if __name__ == "__main__":
    main()