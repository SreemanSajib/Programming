# A9_T4.py


TEMP_MIN = -273.15
TEMP_MAX = 10000.0

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    try:
        c = float(feed)
    except ValueError:
        raise ValueError("could not convert string to float: '{}'".format(feed))

    if c < TEMP_MIN or c > TEMP_MAX:
        raise Exception("'{}' temperature out of range.".format(c))

    return c

def main() -> None:
    print("Program starting.")
    try:
        c = collectCelsius()
        print("You inserted {:.1f} °C".format(c))
    except Exception as e:
        print("Error! {}".format(e))
    print("Program ending.")

if __name__ == "__main__":
    main()
