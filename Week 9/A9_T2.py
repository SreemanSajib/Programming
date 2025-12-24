# A9_T2.py


import sys

def main() -> None:
    print("Program starting.")
    code = int(input("Insert exit code(0-255): "))

    if code < 0:
        code = 0
    if code > 255:
        code = 255

    if code == 0:
        print("Clean exit")
    else:
        print("Error code")

    sys.exit(code)


if __name__ == "__main__":
    main()
