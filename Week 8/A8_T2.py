

def main():
    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            a = float(input("Insert first addend value: "))
            b = float(input("Insert second addend value: "))
            print(f"{a} + {b} = {a + b}")

        elif choice == "2":
            a = float(input("Insert minuend value: "))
            b = float(input("Insert subtrahend value: "))
            print(f"{a} - {b} = {a - b}")

        elif choice == "3":
            a = float(input("Insert multiplicand value: "))
            b = float(input("Insert multiplier value: "))
            print(f"{a} * {b} = {a * b}")

        elif choice == "4":
            a = float(input("Insert dividend value: "))
            b = float(input("Insert divisor value: "))
            print(f"{a} / {b} = {a / b}")

        elif choice == "0":
            print("Exiting program.")
            break

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
