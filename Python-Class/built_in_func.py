import random
import math
import os

def main():
    # Using random.choice() to select a random element from a list
    colors = ['red', 'blue', 'green', 'yellow']
    random_color = random.choice(colors)
    print("Random color:", random_color)

    # Using math.sqrt() to calculate the square root of a number
    number = 16
    square_root = math.sqrt(number)
    print("Square root of", number, ":", square_root)

    # Using os.getcwd() to get the current working directory
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)

if __name__ == "__main__":
    main()
