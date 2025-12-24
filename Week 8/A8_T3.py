

def read_values(filename):
    with open(filename, "r") as f:
        return [float(line.strip()) for line in f if line.strip()]

def main():
    print("Program starting.")
    values = []

    while True:
        print("\nOptions:")
        print("1 - Read values")
        print("2 - Amount of values")
        print("3 - Calculate sum of values")
        print("4 - Calculate average of values")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            filename = input("Insert filename: ")
            values = read_values(filename)

        elif choice == "2":
            print(f"Amount of values {len(values)}")

        elif choice == "3":
            print(f"Sum of values {round(sum(values), 1)}")

        elif choice == "4":
            avg = sum(values) / len(values)
            print(f"Average of values {round(avg, 1)}")

        elif choice == "0":
            print("Exiting program.")
            break

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
