# Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

# Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

# Example program run:

# Program starting.
print("Program starting.")
# Insert fahrenheits: 50
Temp = float(input("Insert farrenheits: "))
Celcius = (Temp - 32) /1.8
Celcius = round(Celcius, 1)
# 50.0°F is 10.0°C
print(f"{Temp}°F is {Celcius}°C")
print("Program ending.")