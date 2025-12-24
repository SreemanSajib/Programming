# A10_T1 Read and display data


def read_values(filename: str) -> list[str]:
    values: list[str] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s != "":
                values.append(s)
    return values


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = read_values(filename)

    print("\n# ---- Vertically ---- #")
    for v in values:
        print(v)

    print("\n# ---- Horizontally ---- #")
    print(", ".join(values))

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
