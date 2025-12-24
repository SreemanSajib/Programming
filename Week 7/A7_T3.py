
# Work need to be done***


WEEKDAYS: tuple[str] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')

    # 0. Clear rows list just in case
    PRows.clear()

    # 1. Open filehandle
    with open(PFilename, "r", encoding="utf-8") as f:
        first_line = True

        # 2. Read filehandle line-by-line
        for line in f:
            # 2.1. Skip first line (header row)
            if first_line:
                first_line = False
                continue

            # 2.2. Check if line is empty '\n'
            if line == "\n":
                continue

            # 2.3. Add non-empty datarow without newline at the end
            PRows.append(line.rstrip("\n"))
    # 3. Close filehandle (done automatically by with)
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    # Append results to the PResults list
    PResults.clear()

    # Initialise helper list
    weekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]

    # Iterate rows with i
    for row in PRows:
        # Iterate WEEKDAYS with j
        for i, weekday in enumerate(WEEKDAYS):
            # Check if the row starts with the weekday name
            if row.startswith(weekday):
                # Count the day in proper place
                weekdayTimestampAmount[i] += 1
                break

    # Iterate WEEKDAYS with i and append the daily results
    for i, weekday in enumerate(WEEKDAYS):
        PResults.append(f"-- {weekday} {weekdayTimestampAmount[i]} stamps")

    # Clear the helper list (not strictly needed, but follows the idea)
    weekdayTimestampAmount.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis. ###")
    # Iterate results and print for the user
    for line in PResults:
        print(line)
    print("### Timestamp analysis. ###")
    return None


def main() -> None:
    print("Program starting.")

    # 1. Initialise rows list
    rows: list[str] = []
    # 1.2. Initialise results list
    results: list[str] = []

    # 2.1. Ask user to define filename
    filename = input("Insert filename: ")

    # 2.2. Read file
    readFile(filename, rows)

    # 2.3. Analyse rows
    analyseTimestamps(rows, results)

    # 2.3. Display results
    displayResults(results)

    # 3.1. Clear lists
    rows.clear()
    results.clear()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
