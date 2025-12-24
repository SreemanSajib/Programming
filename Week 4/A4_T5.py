print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

error_found = False

# Rule 1: start must be less than stop
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    error_found = True

# Rule 2: inspection must be within range
if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    error_found = True

# If any rule failed, skip loops
if error_found:
    print("\nProgram ending.")
    exit()

# --- FIRST LOOP (break) ---
print("\nFirst loop - inspection with break:")
for i in range(start, stop):
    if i == inspection:
        break
    if i < stop - 1:
        print(i, end=" ")
    else:
        print(i, end="")

print("")  # new line

# --- SECOND LOOP (continue) ---
print("Second loop - inspection with continue:")
for i in range(start, stop):
    if i == inspection:
        continue
    if i < stop - 1:
        print(i, end=" ")
    else:
        print(i, end="")

print("\n\nProgram ending.")
