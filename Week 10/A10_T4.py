# A10_T4 Merge sort (TEST TASK)

import sys


def read_ints(filename: str) -> list[int]:
    nums: list[int] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                nums.append(int(s))
    return nums


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = k = 0
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or ((not PAsc) and PLeft[i] >= PRight[j]):
            PMerge[k] = PLeft[i]
            i += 1
        else:
            PMerge[k] = PRight[j]
            j += 1
        k += 1

    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1

    return None


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return None

    temp = [0] * len(PValues)

    def _sort(lo: int, hi: int) -> None:
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        _sort(lo, mid)
        _sort(mid, hi)

        left = PValues[lo:mid]
        right = PValues[mid:hi]
        merge(left, right, temp[lo:hi], PAsc)

        # copy merged slice back into original list
        PValues[lo:hi] = temp[lo:hi]

    _sort(0, len(PValues))
    return None


def main() -> None:
    print("Program starting.")
    filename = sys.argv[1] if len(sys.argv) == 2 else input("Insert filename: ")
    values = read_ints(filename)

    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    asc = values.copy()
    mergeSort(asc, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc))}")

    desc = values.copy()
    mergeSort(desc, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc))}")

    print("Program ending.")


if __name__ == "__main__":
    main()
