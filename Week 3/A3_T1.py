# Make Python program and implement if-statements in proper places.

#     Ask user to insert two integers
#     Compare the integers and then announce the greater number
#     Create sum of the two integers
#     Check the parity of the sum (see modulo-operator ‘%’)

# Other possible output variants:

#     Integer comparison
#         Integers are the same.
#         First integer is greater.
#     Parity check
#         Sum is even.
# Program starting.
print("Program starting.\n Insert two integers.")
# Insert two integers.
# Insert first integer: 2
# Insert second integer: 3
Feed1 = int(input("Insert first integer: "))
Feed2 = int(input("Insert second integer: "))
# Comparing inserted integers.
if(Feed1 > Feed2):
    print("First integer is greater.")
# Second integer is greater.
elif(Feed1 < Feed2):
    print("Second integer is greater.")
else: 
    print("Integers are the same.")
print("")
# Adding integers together
print("Adding integers together.")
# 2 + 3 = 5 
Sum = Feed1 + Feed2
print(f"{Feed1} + {Feed2} = {Sum}")
# Checking the parity of the sum...
print("")
print("Checking the parity of the sum...")

remainder = int(Sum % 2)
if (remainder == 0):
    print("Sum is even.")
else: 
    print("Sum is odd.")
# Sum is odd.
# Program ending.