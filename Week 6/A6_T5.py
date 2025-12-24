SEPARATOR = ";"


def readValues(filename):
    """Read integers from a file and return them as a single string separated by SEPARATOR."""
    values = ""

    with open(filename, "r") as file:
        for line in file:
            number_str = line.strip()
            if number_str == "":
                continue  # extra safety

            if values == "":
                values = number_str
            else:
                values += SEPARATOR + number_str

    return values


def analyseValues(values_str):
    """Take a SEPARATOR-separated string of integers and return a full CSV block as a string."""
    parts = values_str.split(SEPARATOR)

    count = 0
    total = 0
    greatest = None

    for part in parts:
        number = int(part)
        count += 1
        total += number
        if greatest is None or number > greatest:
            greatest = number

    average = total / count

    # Build the exact string the tests expect:
    # "Count;Sum;Greatest;Average\n<values...>\n"
    header = "Count;Sum;Greatest;Average"
    data_line = "{};{};{};{:.2f}".format(count, total, greatest, average)
    result = header + "\n" + data_line + "\n"
    return result


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    print("#### Number analysis - START ####")
    print('File "{}" results:'.format(filename))

    # Read and analyse values
    values_str = readValues(filename)
    csv_block = analyseValues(values_str)

    # Print the CSV result exactly once
    print(csv_block, end="")  # csv_block already ends with a newline
    print()  # extra blank line before END marker

    print("#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()