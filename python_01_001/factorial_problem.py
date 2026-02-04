
get_user_input = int(input("The computer should calculate the factorial of... "))
# This uses for loop to get factorial
def get_factorial(n):
    result = 1

    if (n<=2):
        return n

    elif(n<0):
        return f"Factorial is not defined for {n}"

    for i in range(1,n+1):

        # if (i==0):
        #     continue
        # # Skips the iteration if i==0
        result *=i
    print(result)
    return result

get_factorial(get_user_input)


# This uses recursive method to get factorial
def recursive_get_factorial(n):
    result =1
    if(n<2):
        return result
    elif (n<0):
        return f"Factorial is not defined for {n}"
    result *= n

    return recursive_get_factorial(n-1)

# recursive_get_factorial(get_user_input)


# This uses while loop to get factorial
def while_get_factorial(n):
    i=1
    result=1
    while(i<=n):
        result *=i
        i+=1
    return result

# while_get_factorial(12)