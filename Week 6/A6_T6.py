# T6 – Caesar cipher / ROT13

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(ch, alphabets):
    """Shift a single character by 13 positions inside the given alphabet string."""
    if ch in alphabets:
        idx = alphabets.index(ch)
        return alphabets[(idx + 13) % len(alphabets)]
    return ch


def rot13(text):
    """Apply ROT13 to the whole text (keeps non-letters like spaces and newlines)."""
    result_chars = []
    for ch in text:
        if ch in LOWER_ALPHABETS:
            result_chars.append(shiftCharacter(ch, LOWER_ALPHABETS))
        elif ch in UPPER_ALPHABETS:
            result_chars.append(shiftCharacter(ch, UPPER_ALPHABETS))
        else:
            result_chars.append(ch)
    return "".join(result_chars)


def writeFile(filename, content):
    """Write the given content string to the given filename."""
    # NOTE: tests expect encoding="UTF-8" exactly (uppercase)
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(content)


def main():
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")

    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)

    # Cipher all collected lines using rot13
    ciphered_lines = [rot13(line) for line in lines]

    # First show ciphered text on screen
    print("#### Ciphered text ####")
    for line in ciphered_lines:
        print(line)

    # Then show header again and ask for filename
    print("#### Ciphered text ####")
    filename = input("Insert filename to save: ")

    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
        print("Program ending.")
        return None

    # Build file content (each line on its own line, no extra newline at end)
    content = "\n".join(ciphered_lines) if ciphered_lines else ""

    # Use the required helper function
    writeFile(filename, content)

    print("Ciphered text saved!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()