# Request two numbers from the user and assign them to two variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform operations on those two variables
print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1 / num2)
print("Remainder division: ", num1 % num2)

# Use comparison operators to determine which of the two numbers is greater and print the results
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num2, "is greater than", num1)
else:
    print("The numbers are equal")

# Create a mutable list type numbers 0-99
num_list = list(range(100))

# Determine if each of the numbers entered by the user are in the list
if num1 in num_list and num2 in num_list:
    print("Both numbers are in the list")
elif num1 in num_list or num2 in num_list:
    print("One number is in the list")
else:
    print("Neither number is in the list")