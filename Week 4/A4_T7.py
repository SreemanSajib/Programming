print("Program starting.")
print()
print("Check multiplicative persistence.")
num = input("Insert an integer: ")

steps = 0
while len(num) > 1: 
    digits = [int(d) for d in num]

    exp = " * ".join(num)
    product = 1
    for d in digits:
        product *= d
    print(f"{exp} = {product}")

    num = str(product)
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")