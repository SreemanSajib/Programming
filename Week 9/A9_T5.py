# A9_T5.py


def read_byte(name: str) -> int:
    raw = input(f"Insert {name}: ")

    try:
        num = float(raw)
    except ValueError:
        raise ValueError("non-numeric")

    if not num.is_integer():
        raise ValueError("not-integer")

    val = int(num)
    if val < 0 or val > 255:
        raise ValueError("out-of-range")

    return val

def main() -> None:
    print("Program starting.")

    try:
        r = read_byte("red")
        g = read_byte("green")
        b = read_byte("blue")

        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        print("- Hex #{:02x}{:02x}{:02x}".format(r, g, b))

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()
