# This marks the beginning of a python script. 

PI: float = 3.14
area : float = 0


def area_of_circle()-> float:
    radius: float = float(input("Enter the value for radius: "))
    return PI*(radius**2)


def area_of_square()-> float:
    length: float = float(input("Enter the length of one side: "))
    return length**2


def area_of_rectangle() -> float:
    length: float= float(input("Enter the value of length: "))
    breadth: float= float(input("Enter the value for "))
    return length*breadth


def area_of_triangle_1()->float:
    side_a : float = float(input("Enter the length of side a: "))
    side_b : float = float(input("Enter the length of side b: "))
    side_c : float = float(input("Enter the length of side c: "))
    semi_perimeter_s : float = (side_a+side_b+side_c)/2
    s = semi_perimeter_s
    area = (s*(s-side_a)*(s-side_b)*(s-side_c))**(1/2)
    return area


# def diff(a,b):
#     return a-b

def perimeter_of_square() -> float:
    side_length: float = float(input("Enter the lenth of a side: "))
    return 4*side_length


def average_of() -> float:
    sum_of: float = 0
    count = 0
    total_inputs_to_take : int = int(input("Enter the number of inputs to be taken: "))
    for i in range(1, total_inputs_to_take+1):
        num: float = float(input("Enter your number"))
        sum_of +=num
        count +=1
    return sum_of/count


#                           Needs ammendment

# def greater_than()-> float:
#     num1: float = float(input("Enter your first number: "))
#     num2: float = float(input("Enter your second number: "))

#     if (num1< num2):
#         return num2
#     elif (num1>num2):
#         return num1
#     elif (num1 == num2):
#         print("both are equal.")
#         return num1
#     else: 
#         print("somethign went wrong!!")
#     return 0


