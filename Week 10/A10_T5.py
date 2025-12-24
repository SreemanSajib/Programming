# A10_T5 Recursive factorial

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)


def main() -> None:
    print("Program starting.")
    n = int(input("Insert factorial: "))
    result = recursiveFactorial(n)
    print(f"Factorial {n}!")
    print(f"{n}! = {result}")
    print("Program ending.")


if __name__ == "__main__":
    main()
