import os

def check_file_permissions(filename):
    try:
        with open(filename, 'r'):
            print(f"Read permission is granted on file: {filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print(f"No read permission on file: {filename}")

# Usage example
check_file_permissions("/Users/owenjohnson/Documents/GitHub/python/Python-Class/bruh.txt")

#!/usr/bin/python3
#file i/o assignment example
def main():
    #open files
    p1 = open("/Users/owenjohnson/Documents/GitHub/python/Python-Class/bruh.txt", 'r')
    p2 = open("/Users/owenjohnson/Documents/GitHub/python/Python-Class/bruh2.txt", 'r')
    finished = open("output.txt", "w")

    part1, part2 = list(), list()
    
    #read each line of the file
    for line in p1:
        part1.append(line)\

    for line in p2:
        part2.append(line)

    for x, y in zip(part1, part2):
        print(x, file = finished, end = '')
        print(y, file = finished, end = '')

main()