# Print each letter of the word
word = input("Enter a word: ")
print("Each letter of the word:")
for letter in word:
    print(letter)

# Print each letter of the word in reverse order
print("Each letter of the word in reverse:")
for letter in reversed(word):
    print(letter)

# Print the word in reverse
reverse_word = word[::-1]
print("The word in reverse order:", reverse_word)

# Count the occurrences of a letter
count_letter = input("Enter a letter to count: ")
count = 0
for letter in word:
    if letter == count_letter:
        count += 1
print(f"The letter {count_letter} appears {count} times in the word.")
