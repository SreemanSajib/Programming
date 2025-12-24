# Make Python program, which prompts user to insert two words. Print the length of each word and then compound them together. Put single quotes around the compound word.

print("Program starting.")
Word1= input("Insert first word: ")
Word2= input("Insert second word: ")

print(f"1st word is {len(Word1)} characters long.")
print(f"2nd word is {len(Word2)} characters long.")

print(f"Words together makes one closed compound \'{Word1 + Word2}\'")
print("Program ending.")