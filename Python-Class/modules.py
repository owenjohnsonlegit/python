import math

# Get the radius of the sphere from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere
volume = (4/3) * math.pi * radius**3

# Calculate the area of the sphere
area = 4 * math.pi * radius**2

# Print the volume rounded to 2 decimal places
print("Volume of the sphere:", round(volume, 2))

# Print the area rounded to 2 decimal places
print("Area of the sphere:", round(area, 2))


# Sources
# https://www.google.com/search?q=how+to+calculate+volume+of+a+sphere&rlz=1C5CHFA_enUS996US996&oq=how+to+calculate+volume+of+a+sphere&aqs=chrome..69i57j0i512l6j0i22i30l3.4962j0j7&sourceid=chrome&ie=UTF-8

# https://www.google.com/search?q=how+to+calculate+area+of+a+sphere&rlz=1C5CHFA_enUS996US996&sxsrf=APwXEdcPwvLcOoesEUCdE1gAcKs6FmD1mw%3A1684185395418&ei=M6FiZJ2SGfjmkPIPpa6I-AU&ved=0ahUKEwjd9-rBn_j-AhV4M0QIHSUXAl8Q4dUDCBA&uact=5&oq=how+to+calculate+area+of+a+sphere&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yCwgAEAgQHhDxBBAKMggIABAIEB4QCjIICAAQigUQhgM6CggAEEcQ1gQQsAM6CggAEIoFELADEEM6BggAEAcQHjoICAAQCBAHEB46CgghEKABEMMEEAo6BwgAEA0QgAQ6CAgAEAgQHhANOg0IABAIEB4QDRDxBBAKOg0IABAIEAcQHhDxBBAKOgoIABAIEAcQHhAKSgQIQRgAUMADWJIPYMYQaARwAXgAgAFuiAG_BJIBAzUuMpgBAKABAcgBCsABAQ&sclient=gws-wiz-serp