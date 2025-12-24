# A9_T3.py


import os
import sys

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    if not os.path.exists(filename):
        print("Error! File '{}' doesn't exist.".format(filename))
        sys.exit(1)

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

    print("Program ending.")


if __name__ == "__main__":
    main()
