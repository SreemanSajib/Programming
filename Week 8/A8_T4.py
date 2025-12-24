
from datetime import datetime

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def read_timestamps(filename):
    out = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                out.append(datetime.strptime(s, "%Y-%m-%d %H:%M"))
    return out

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = read_timestamps(filename)

    while True:
        print("\nOptions:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month")
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            year = int(input("Insert year: "))
            count = sum(1 for t in timestamps if t.year == year)
            print(f"Amount of timestamps during year '{year}' is {count}")

        elif choice == "2":
            month_name = input("Insert month: ")
            month_num = MONTHS.index(month_name) + 1
            count = sum(1 for t in timestamps if t.month == month_num)
            print(f"Amount of timestamps during month '{month_name}' is {count}")

        elif choice == "3":
            weekday_name = input("Insert weekday: ")
            weekday_num = WEEKDAYS.index(weekday_name)
            count = sum(1 for t in timestamps if t.weekday() == weekday_num)
            print(f"Amount of timestamps during weekday '{weekday_name}' is {count}")

        elif choice == "0":
            print("Exiting program.")
            break

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
