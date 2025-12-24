print("Program starting.")
print("This program analyses a list of names from a file.")

# Ask user for filename
filename = input("Insert filename to read: ")

print(f'Reading names from "{filename}".')
print("Analysing names...")

name_count = 0
total_length = 0
shortest = None
longest = None

# Read file and analyse
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()          # remove whitespace and newline
        if name == "":               # skip empty lines
            continue

        length = len(name)
        name_count += 1
        total_length += length

        if shortest is None or length < shortest:
            shortest = length

        if longest is None or length > longest:
            longest = length

print("Analysis complete!")

# Calculate average length
average_length = total_length / name_count
average_str = "{:.2f}".format(average_length)   # 2 decimal precision

# Print report
print("#### REPORT BEGIN ####")
print(f"Name count - {name_count}")
print(f"Shortest name - {shortest} chars")
print(f"Longest name - {longest} chars")
print(f"Average name - {average_str} chars")
print("#### REPORT END ####")

print("Program ending.")
