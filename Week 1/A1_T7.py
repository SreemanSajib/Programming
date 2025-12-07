'''Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”'''

print("Calculate fuel consumtion.")
Feed1 = input("Enter travel distance(kilometers): ")
Distance= int(Feed1)

Feed2= input("Enter fuel usage(liters): ")
FuelUsage= int(Feed2)

Consumtion = int((FuelUsage / Distance) * 100 )
print(f"Fuel consumtion is {Consumtion} l per 100 km.")
