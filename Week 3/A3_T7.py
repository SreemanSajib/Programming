print("Program starting.")
print("Testing decision structures.")

# Prompt for integer
value = int(input("Insert an integer: "))

# Display menu
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

choice = input("Your choice: ")

# OPTION 1: Multi-branched decision (if / elif / elif)
if choice == "1":
    print("Using one multi-branched decision structure.")
    result = value

    if result >= 400:
        result += 44
    elif result >= 200:
        result += 22
    elif result >= 100:
        result += 11

    print(f"Result is {result}")

# OPTION 2: Independent if-statements
elif choice == "2":
    print("Using multiple independent if-statements.")
    result = value

    if result >= 400:
        result += 44
    if result >= 200:
        result += 22
    if result >= 100:
        result += 11

    print(f"Result is {result}")

# OPTION 0: Exit
elif choice == "0":
    print("Exiting...")

# Unknown selection
else:
    print("Unknown option.")

print("\nProgram ending.")
