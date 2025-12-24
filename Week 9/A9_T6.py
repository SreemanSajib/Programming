# A9_T6.py

def save_lines(lines: list[str]) -> None:
    filename = input("Insert filename: ")
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def print_menu() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    lines: list[str] = []

    try:
        while True:
            print_menu()
            choice = input("Your choice: ")

            if choice == "1":
                txt = input("Insert text: ")
                lines.append(txt)

            elif choice == "2":
                save_lines(lines)

            elif choice == "0":
                break

    except KeyboardInterrupt:
        if len(lines) == 0:
            print("Keyboard interrupt! Program closing suddenly.")
        else:
            print("Keyboard interrupt and unsaved progress!")
            ans = input("Save before quit(y/n)?: ").strip().lower()
            if ans == "y":
                save_lines(lines)

    print("Program ending.")


if __name__ == "__main__":
    main()
