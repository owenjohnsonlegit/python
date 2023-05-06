# Calculate windchill and return the result
def windChill(temp, speed):
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (0.4275 * temp * (speed ** 0.16))
    return wind_chill

# Get input from user, call the windChill function, and display end result to the user
def main():
    temp = float(input("Enter the temperature in Fahrenheit: "))
    speed = float(input("Enter the wind speed in miles per hour: "))
    wind_chill = windChill(temp, speed)
    wind_chill_rounded = round(wind_chill)
    print("The temperature including wind chill is", wind_chill_rounded, "degrees Fahrenheit.")

if __name__ == '__main__':
    main()