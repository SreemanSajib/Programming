# A9_T1.py

def main() -> None:
    print("Program starting.")

    total = 0.0
    while True:
        raw = input("Insert a floating-point value (0 to stop): ")
        try:
            val = float(raw)
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(raw))
            continue

        if val == 0.0:
            break

        total += val

    print("Final sum is {:.2f}".format(total))
    print("Program ending.")


if __name__ == "__main__":
    main()
