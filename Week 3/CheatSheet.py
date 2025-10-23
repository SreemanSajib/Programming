print("Welcome to the app")
Temp = int(input("What is the Temperature of your CPU?"))

# if Temp > 80:
#     print("Warning! The temparature is too high!")
# else: 
#     print("Everything cool! Keep cooding :) ")

# > greater
# < less
# >= greater or equal
# <= less or equal
# != not equal to 

#Make a program, which tests if the user input is odd or even. 

# print("Give a Integer Number: ")
# Number = int(input("Give a integer Number: ")) 

# remainder= Number % 2

# if remainder == 0:
#     print("The number is even")
# else: 
#     print("The number is odd")

if Temp> 80: 
    if Temp > 90: 
        print("The CPU is toast. Get your fire extinguisher.")
    else: 
        print("Warning! Temperature is too high")
else: 
    print("All Good, go ahead.")

if Temp > 90:
    print("The CPU is toast. Get your fire extinguisher.")
elif Temp > 80: 
    print("Warning! Temparature is too High")
else: 
    print("All good, go ahead.")

# Make a program, which asks the user for two names. Then tests if the length of the first name is longer, 
#shorter or equal length to the second name. hint len()

# name1= input("Enter the first name: ")
# name2 = input("Enter the second name: ")
# Len1= len(name1)
# Len2= len(name2)

# if Len1 > Len2:
#     print(f"The first name {name1} is longer than second name {name2}")
# elif Len1< Len2:
#     print(f" The first name {name1} is shorter than the second name {name2}")
# else: 
#     print("Both names are equal")

Town = "Lahti"
Street = "Mukkulankatu"
Building = 19

if(Town== "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are at LAB!")
elif(Town =="Lahti" and (Street != "Mukkulankatu" or Building != 19)):
    print("You are in the correct town, but check the street address")
elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building ==19):
    print("You are completely lost!")   


import random

print(random.random())
RandomInteger = random.randint(1,10)
print(RandomInteger)


