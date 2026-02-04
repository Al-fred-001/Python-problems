# This marks the beginning of a python script. 
import cosine_function, sine_function
from sine_function import calc_factorial, exponent_to, degree_to_radian, sine_of_x
from cosine_function import cosine_of_x



def tangent_of_x(n):
    solution = (sine_of_x(n)/float(cosine_of_x(n)))
    return round(solution, 2)



def main():
    input_degrees = int(input("Enter the value of x (in degrees): "))
    print(tangent_of_x(input_degrees))


if __name__ =="__main__":
    main()