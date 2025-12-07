'''Make a Python program, which prompts the user name and two floating numbers. Multiply the inserted numbers to get product. Round the product in two decimal precision.'''


print("Program starting.")
name = input("What is your name: ")
num1= float(input("Enter a floating point number: "))
num2 = float(input("Enter second floating point number: "))

print(f"{name} you gave numbers {num1} and {num2}")
print(f"Multiplying first and second number will result in product {num1 * num2}")