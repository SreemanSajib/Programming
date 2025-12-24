# A10_T2 Aggregate data


def read_ints(filename: str) -> list[int]:
    nums: list[int] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s != "":
                nums.append(int(s))
    return nums


def sum_of_values(values: list[int]) -> int:
    return sum(values)


def product_of_values(values: list[int]) -> int:
    product = 1
    for n in values:
        product *= n
    return product


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    nums = read_ints(filename)

    print("# --- sum of numbers --- #")
    print(sum_of_values(nums))

    print("# --- product of numbers --- #")
    print(product_of_values(nums))

    print("Program ending.")


if __name__ == "__main__":
    main()
