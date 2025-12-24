# A10_T6 Sorting algorithm speed tests

import copy
import time
from typing import Callable


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


def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    mid = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + mid + quickSort(right)


def measureSortingTimePSorting(PSorting: Callable, PArr: list[int]) -> int:
    start = time.perf_counter_ns()
    _ = PSorting(PArr)
    end = time.perf_counter_ns()
    return end - start


def main() -> None:
    print("Program starting.")
    values: list[int] = []
    results_text = ""
    dataset_name = ""

    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            dataset_name = input("Insert dataset filename: ").strip()
            values = read_ints(dataset_name)
            print("Dataset loaded.")

        elif choice == "2":
            if not values:
                print("Load dataset first (option 1).")
                continue

            # built-in sorted
            t_sorted = measureSortingTimePSorting(lambda arr: sorted(arr), copy.deepcopy(values))

            # bubble sort (in-place)
            def bubble_wrapper(arr: list[int]) -> list[int]:
                bubbleSort(arr, True)
                return arr

            t_bubble = measureSortingTimePSorting(bubble_wrapper, copy.deepcopy(values))

            # quick sort (returns new)
            t_quick = measureSortingTimePSorting(lambda arr: quickSort(arr), copy.deepcopy(values))

            results_text = (
                f"Measured speeds for dataset '{dataset_name}':\n"
                f"Built-in sorted: {t_sorted} ns\n"
                f"Quick sort: {t_quick} ns\n"
                f"Bubble sort: {t_bubble} ns\n"
            )
            print(results_text, end="")

        elif choice == "3":
            if not results_text:
                print("No results to save. Run option 2 first.")
                continue
            if not dataset_name:
                print("No dataset name known. Load dataset first.")
                continue

            out_name = dataset_name.replace(".txt", "_Results.txt")
            with open(out_name, "w", encoding="utf-8") as f:
                f.write(results_text)
            print(f"Saved results in file: {out_name}")

        elif choice == "0":
            print("Exiting program.")
            print("Program ending.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
