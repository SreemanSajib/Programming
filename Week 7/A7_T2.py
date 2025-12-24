print("Program starting.")

raw_input_str = input("Insert comma separated integers: ")

parts = raw_input_str.split(",")
valid_numbers: list[int] = []

for part in parts:
    part = part.strip()
    try:
        number = int(part)
        valid_numbers.append(number)
    except ValueError:
        print(f"Invalid value detected: {part}")

if len(valid_numbers) == 0:
    print("No valid integers to analyze.")
else:
    count = len(valid_numbers)
    total_sum = sum(valid_numbers)
    parity = "even" if total_sum % 2 == 0 else "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total_sum} and it's {parity}")

print("Program ending.")
