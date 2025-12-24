# A6_T7 – Messages from the Four Emperors

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

PLACE_NAMES = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace",
}


def rot13_char(ch: str) -> str:
    if ch in LOWER_ALPHABETS:
        idx = LOWER_ALPHABETS.index(ch)
        return LOWER_ALPHABETS[(idx + 13) % 26]
    if ch in UPPER_ALPHABETS:
        idx = UPPER_ALPHABETS.index(ch)
        return UPPER_ALPHABETS[(idx + 13) % 26]
    return ch


def rot13(text: str) -> str:
    return "".join(rot13_char(c) for c in text)


def read_progress(filename: str = "player_progress.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    last_row = lines[-1]  # header is first, last is latest progress
    current_str, next_str, passphrase_cipher = last_row.split(";")
    current_loc = int(current_str)
    next_loc = int(next_str)
    return current_loc, next_loc, passphrase_cipher


def append_progress(new_row: str, filename: str = "player_progress.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n" + new_row.strip())


def process_message(current_loc: int, next_loc: int, passphrase_cipher: str):
    # Compute filenames
    cipher_filename = f"{next_loc}_{passphrase_cipher}.gkg"

    # Read cipher file
    with open(cipher_filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # First line: new progress row (still "ciphered" / encoded passphrase)
    progress_row = lines[0]
    append_progress(progress_row)

    # Remaining lines: ciphered message to decode
    cipher_message_lines = lines[1:]

    plain_passphrase = rot13(passphrase_cipher)
    plain_filename = f"{next_loc}-{plain_passphrase}.txt"

    with open(plain_filename, "w", encoding="utf-8") as out:
        for line in cipher_message_lines:
            out.write(rot13(line) + "\n")

    return plain_passphrase


def main():
    print("Travel starting.")

    current_loc, next_loc, passphrase_cipher = read_progress()
    current_place = PLACE_NAMES.get(current_loc, "Unknown place")
    next_place = PLACE_NAMES.get(next_loc, "Unknown place")

    print(f"Currently at {current_place}.")
    print(f"Travelling to {next_place}...")
    print(f"...Arriving to the {next_place}.")
    print("Passing the guard at the entrance.")

    plain_passphrase = rot13(passphrase_cipher)
    # Shout the passphrase (nicely formatted)
    shout = plain_passphrase.capitalize() + "!"
    print(f"\"{shout}\"")

    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    # Decode and save message
    _ = process_message(current_loc, next_loc, passphrase_cipher)
    print("Looks like I've got now the plain version copy of the")
    print("Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


if __name__ == "__main__":
    main()
