class housePet:
    fav_pet = "dog"
    fav_pet_sound = "woof woof bark"
    def type_of_pet(fav_pet):
        print("My favorite pet is a {fav_pet}")
    def sound_of_pet(fav_pet, fav_pet_sound):
        print("The sound a {fav_pet} makes is {fav_pet_sound}")

def main(fname):
    print(fname + " is the imposter")
    cool_number = 1
    cool_string = "Bruh"
    print(cool_number)
    print(cool_string)
    print("The variable, cool_number is of type:", type(cool_number))
    print("The variable, cool_string is of type:", type(cool_string))
    global first_number
    first_number = 1
    global second_number
    second_number = 10
    if first_number < second_number:
        print("The first_number variable is less than second_number variable")
    elif first_number > second_number:
        print("The first_number variable is greater than the second_number variable")
    else:
        print("The first_number variable is equal to the second_number variable")



main("John")

# def new_function(first_number, second_number):
#     print(list(range(first_number, second_number)))


def brand_new_function(first_number, second_number):
    num_list = []
    for i in range(first_number+1, second_number):
        num_list.append(i)
    
    print(f'First number: {first_number} Second number: {second_number}')
    print(f'The numbers between {first_number} and {second_number} are {num_list}')

brand_new_function(first_number, second_number)
print("NOTE: Now I'm going to change the values of first_number and second_number")
first_number = 5
second_number = 11
brand_new_function(first_number, second_number)

main("Landon")
# Sources
# https://stackoverflow.com/questions/68478874/print-two-numbers-between-two-integers-python
# https://www.tutorialspoint.com/how-do-i-call-a-variable-from-another-function-in-python
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_variables_global.asp#:~:text=The%20global%20Keyword,can%20use%20the%20global%20keyword.
# https://www.w3schools.com/python/python_functions.asp