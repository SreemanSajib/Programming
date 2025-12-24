DELIMITER = ";"

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
]


class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0


class DAY_USAGE:
    def __init__(self):
        self.usage: float = 0.0
        self.cost: float = 0.0


def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')

    PTimestamps.clear()

    with open(PFilename, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            if first:       # skip header
                first = False
                continue

            row = line.rstrip("\n")
            if row == "":
                continue

            columns = row.split(DELIMITER)

            ts = TIMESTAMP()
            ts.weekday = columns[0]
            ts.hour = columns[1]
            ts.consumption = float(columns[2])
            ts.price = float(columns[3])

            PTimestamps.append(ts)
            columns.clear()


def analyseTimestamps(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    # initialize daily summary
    daily: list[DAY_USAGE] = []
    for _ in WEEKDAYS:
        daily.append(DAY_USAGE())

    # accumulate usage and cost day-by-day
    for ts in PTimestamps:
        if ts.weekday in WEEKDAYS:
            index = WEEKDAYS.index(ts.weekday)
            daily[index].usage += ts.consumption
            daily[index].cost += ts.consumption * ts.price

    # produce results list of strings
    PResults.clear()
    for i, day in enumerate(WEEKDAYS):
        PResults.append(
            f" - {day} usage {daily[i].usage:.2f} kWh, cost {daily[i].cost:.2f} €"
        )


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for line in PResults:
        print(line)
    print("### Electricity consumption summary ###")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    timestamps: list[TIMESTAMP] = []
    results: list[str] = []

    readFile(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)

    timestamps.clear()
    results.clear()

    print("Program ending.")


if __name__ == "__main__":
    main()
