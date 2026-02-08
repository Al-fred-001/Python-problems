# This marks the beginning of a python script . 


'''
Remaining: To ask the user on whether or not to store the password generated or to generate another one.
'''



import random 
import datetime
from pathlib import Path

small_letters = 'qwertyuiopasdfghjklzxcvbnm'
capital_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '0123456789'
symbols = '!@#$%&*?/;:+-=_'

# symbols = '!@#%^&*()_+-=[}]{:;"?/|,<>.`~'  
# array_of_characters = [small_letters, capital_letters, numbers, symbols]
# print(array_of_characters)

print("\n--Initializing Password Generator--\n")


def shuffle_list(list_of_characters: list)-> list:
    count: int = 0;
    random_numbers_list: list [int] = []
    shuffled_output: list = []

    while (count <len(list_of_characters)):

        random_number: int = random.randint(0,len(list_of_characters)-1) 
        # list index range : 0 to len(list)-1 

        if (random_number not in random_numbers_list):
            temporary  = list_of_characters[random_number]
            shuffled_output.append(temporary)
            random_numbers_list.append(random_number)
            count +=1

        else:
            continue

    return shuffled_output


# handles a standard that is set while generating password.
def get_standardized_amount(n):

    #descriptive naming but pretty lenghty names :(
    quantity_of_small_letters = int(n/2)
    qty_of_capital_letters = int((n)/6)
    qty_of_digits = qty_of_capital_letters
    total_characters = quantity_of_small_letters + qty_of_capital_letters + qty_of_digits


    if (total_characters<n and total_characters + qty_of_capital_letters != n):
        qty_of_symbols = qty_of_capital_letters
    elif (total_characters == n):
        quantity_of_small_letters -=2
        qty_of_symbols = 2
    else:
        qty_of_symbols = n - total_characters
    if (total_characters+qty_of_symbols !=n):
        qty_of_symbols += n-(total_characters+qty_of_symbols)
    
    return quantity_of_small_letters,qty_of_capital_letters,qty_of_digits,qty_of_symbols







def get_random_characters():
    characters = []
    while len(characters)==0:
        length_of_password = int(input("Enter the desired length of your password (8 to 40): "))
        a,b,c,d = get_standardized_amount(length_of_password)
        # a, b, c , d are the standardized amount in which characters should be taken.
        # actual meaning of a, b , c, d in function definiton of  get_standardized_amount(n)

        if (length_of_password>=8 and length_of_password<=40):

                for i in range (0, a):
                    random_letter = random.randint(0,25)
                    characters.append(small_letters[random_letter])

                for i in range(0,b):
                    random_letter = random.randint(0,25)
                    characters.append(capital_letters[random_letter])
                
                for i in range(0,c):
                    random_digit = random.randint(0,9)
                    characters.append(numbers[random_digit])
                
                for i in range(0,d):
                    random_symbol = random.randint(0,len(symbols)-1)
                    characters.append(symbols[random_symbol])
    return characters





# The function to be called for password generation
def password_generator()-> str:
    choosen_characters = get_random_characters()
    shuffled_characters = shuffle_list(choosen_characters)
    generated_password = ''.join(shuffled_characters)
    return generated_password

password_generated = password_generator()


now = datetime.datetime.now() # for date and time


user_comment = input("\nWhat should the password be stored as? (Default = Newly generated password) \nYour comment on password: ")
default = "Newly generated password: "
password_for = user_comment if (user_comment !='') else default

if Path("password_generator/password_generated.txt").is_file():
    # appends to the file specified if it exists already in the same folder .
    with open("password_generator/password_generated.txt", 'a') as the_file:
        the_file.write(f"\nThe latest generated password is: {password_generated}\n")

        the_file.write(f"About the password: {password_for}")

        the_file.write(f"\nPassword length = {len(password_generated)}\nCreation date: {datetime.date.today()} \nCreation Time: {now.strftime("%H:%M:%S")}\n")


else:
    # else creates a file specified if it doesn't exist
    with open("password_generator/password_generated.txt", "w") as a_file:
        a_file.write(f"\nThe latest generated password is: {password_generated} \n")
        
        a_file.write(f"About the password: {password_for}")

        a_file.write(f"\nPassword length = {len(password_generated)}\nCreation date: {datetime.date.today()} \nCreation Time: {now.strftime("%H:%M:%S")}\n")


print("\n--Password generated and saved successfully.--\n")