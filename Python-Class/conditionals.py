from ast import operator
from unittest import result

# Start of assignment, Part 1

def shoe_selector():

    usr_input = input("How's the weather today? (options: hot, rain, or snow)")
    
    if usr_input == "hot":
        print("You should wear sandals.")
    elif usr_input == "rain":
        print("You should wear galoshes.")
    elif usr_input == "snow":
        print("You should wear boots.")
    else:
        print("You should wear shoes.")

shoe_selector()

###############################################################################################
# Start of Part 2

def silly_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print("Invalid operator input, options are +, -, *, or /")

num1 = int(input("Give me a number "))
num2 = int(input("Give me another number "))
operator = input("Give me an operator (options: +, -, *, or /) ")
usr_answer = int(input("What's the answer? "))

result = silly_calculator(num1, num2, operator)

if result == usr_answer:
    print("Correct! Good job.")
else:
    print("Incorrect! Looks like there might be an imposter among us...")

silly_calculator(num1, num2, operator)