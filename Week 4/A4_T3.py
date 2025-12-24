print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

i = start
while i <= stop:
    if i < stop:
        print(i, end=" ")
    else:
        print(i, end="")   # Last number without trailing space
    i += 1

print("\n\nProgram ending.")
