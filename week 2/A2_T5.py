# Make a Python program, which prompts for a compound word.

#     Get following aspects from the word
#         Length
#         First character
#         Reversed version e.g. “Suitcase” is reversed “esactiuS”
#     Display the aspects using print commands.
#     Prompt the user to take substring from the existing compound word.
#     Finally print the user specified substring.
# Example program run:

# Program starting.
print("Program starting.")

# Insert a closed compound word: Moonbanana
word = input("Insert a closed compound word: ")
# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
reversed_word = word[::-1]
print(f"The word you inserted is '{word}' and in reverse it is '{reversed_word}'.")
# The inserted word length is 10
length_word = len(word)
print(f"The inserted word length is {length_word}")
# First character is 'M'
print(f"First character is '{word[0]}'")
# Last character is 'a'
# Last_character = word[-1]
print(f"Last character is '{word[-1]}'")

# Take substring from the inserted word by inserting...
print("Take substring from the inserted word by inserting...")
# 1) Starting point: 0
starting_point = int(input("1) Starting point: "))
# 2) Ending point: 4
ending_point = int (input("2) Ending point: "))
# 3) Step size: 1
step_size = int (input("3) Step size: "))
if starting_point < 0 or ending_point > length_word or step_size <= 0:
    print("Invalid input")
    print("Program ending.")
    exit()

substring = word[starting_point:ending_point:step_size]
print(f"The word '{word}' sliced to the defined substring is '{substring}'.")
# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
# Program ending.
print("Program ending.")


