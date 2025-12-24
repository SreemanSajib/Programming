# A10_T3 Bubble sort (TEST TASK)

import sys


def read_ints(filename: str) -> list[int]:
    nums: list[int] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                nums.append(int(s))
    return nums


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (PAsc and PValues[j] > PValues[j + 1]) or ((not PAsc) and PValues[j] < PValues[j + 1]):
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                swapped = True
        if not swapped:
            break
    return None


def main() -> None:
    print("Program starting.")
    filename = sys.argv[1] if len(sys.argv) == 2 else input("Insert filename: ")
    values = read_ints(filename)

    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    asc = values.copy()
    bubbleSort(asc, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc))}")

    desc = values.copy()
    bubbleSort(desc, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc))}")

    print("Program ending.")


if __name__ == "__main__":
    main()
