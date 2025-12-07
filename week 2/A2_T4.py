# Prompt the user to insert the minutes spent on each previous topic task. Calculate the sum and the average. Display those in the example program run format(Note! precision). Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

print("Program starting.")
print("Estimate how many minutes you spent on programming....")

T1= float(input("A1_T1: "))
T2= float(input("A1_T2: "))
T3= float(input("A1_T3: "))
T4= float(input("A1_T4: "))
T5= float(input("A1_T5: "))
T6= float(input("A1_T6: "))
T7= float(input("A1_T7: "))

sum = T1 + T2 + T3 + T4 + T5 + T6 + T7
avg = sum / 7
rounded_avg = round(avg)
print("In total you have spent %.0f minutes on progamming." % sum)
print("Average per task is %.2f min and same rounded to the nearest integer %d min." %(avg, rounded_avg))

print("Program ending.")


