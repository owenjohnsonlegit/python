n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1, 2):
    sum += i

print("The sum of odd integers between 1 and", n, "is", sum)