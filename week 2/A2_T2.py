'''Make a Python program, which prompts user for a car brand and model. After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters.'''

print("Program starting.")
brand= input("Insert car brand: ")
model= input("Insert car model: ")
print("Car brand is", f"\"{brand}\"", sep=" ", end=" ")
print("and the model is", f"'{model}'", sep=" ", end=".\n")
print("Program ending.") 