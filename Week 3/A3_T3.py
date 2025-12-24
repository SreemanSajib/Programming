print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

# Prompt for user name
name = input("Before the menu, please insert your name: ")

# Print menu
print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")

# User choice
choice = input("Your choice: ")

# Handle user choice
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
