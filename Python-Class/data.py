# Create and display the list
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print("List of fruits:", fruits)

# Ask user for another fruit and add it to the end of the list
new_fruit = input("Enter another fruit: ")
fruits.append(new_fruit)
print("Updated list of fruits:", fruits)

# Ask user for a number and display the corresponding fruit
num = int(input("Enter a number: "))
print("Number entered:", num)
if num <= len(fruits):
    print("Fruit corresponding to the number:", fruits[num-1])
else:
    print("Invalid number entered.")

# Add another fruit to the beginning of the list and display the list
fruits.insert(0, "Bananas")
print("Updated list of fruits:", fruits)

# Display all the fruits using a for loop
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Create and display the dictionary
chris_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print("Dictionary:", chris_dict)

# Delete entry for “cake”
chris_dict.pop("cake")
print("Dictionary after deleting 'cake':", chris_dict)

# Add an entry for “fruit” with “Mango”
chris_dict["fruit"] = "Mango"
print("Dictionary after adding 'fruit':", chris_dict)

# Display the dictionary keys and values
print("Dictionary keys:", chris_dict.keys())
print("Dictionary values:", chris_dict.values())

# Display whether or not “cake” is a key in the dictionary
print("Is 'cake' a key in the dictionary?", "cake" in chris_dict)

# Display whether or not “Mango” is a value in the dictionary
print("Is 'Mango' a value in the dictionary?", "Mango" in chris_dict.values())

# Create sets s2, s3 and s4
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

# Display the sets
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)

# Display the union of s2 and s3
print("Union of s2 and s3:", s2.union(s3))

# Display the intersection of s3 and s4
print("Intersection of s3 and s4:", s3.intersection(s4))
