# Work need to be done***

DELIMITER = ";"


class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0


def readFile(PFilename, PTimestamps):
    print(f'Reading file "{PFilename}".')

    PTimestamps.clear()

    with open(PFilename, "r", encoding="utf-8") as f:
        first_line = True
        for line in f:
            # Skip header row
            if first_line:
                first_line = False
                continue

            row = line.rstrip("\n")
            if row == "":
                continue

            columns = row.split(DELIMITER)

            ts = TIMESTAMP()
            ts.weekday = columns[0]
            ts.hour = columns[1]          # e.g. "00", "01"
            ts.consumption = float(columns[2])
            ts.price = float(columns[3])

            PTimestamps.append(ts)
            columns.clear()


def displayTimestamps(PTimestamps):
    print("Electricity usage:")
    for ts in PTimestamps:
        total = ts.consumption * ts.price
        # Hour printed as HH:00, values with two decimals where needed
        print(
            " - {} {}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
                ts.weekday,
                ts.hour,
                ts.price,
                ts.consumption,
                total,
            )
        )


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    timestamps = []
    readFile(filename, timestamps)
    displayTimestamps(timestamps)

    print("Program ending.")


if __name__ == "__main__":
    main()
