def frameWord(PWord):
    # Create frame length: word length + 4 (space + * on each side)
    frame = "*" * (len(PWord) + 4)
    print(frame)
    print(f"* {PWord} *")
    print(frame)
    return None


def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()  # empty line
    frameWord(word)
    print()
    print("Program ending.")
    return None


# Call main
main()
