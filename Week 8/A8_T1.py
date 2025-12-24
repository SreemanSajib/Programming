
import time

def main():
    print("Program starting.")
    pause_time = None   # pause not set initially

    while True:
        print("\nOptions:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            pause_time = float(input("Insert pause duration (s): "))

        elif choice == "2":
            if pause_time is None:
                print("Pause is not set.")
                print("Set pause first.")
            else:
                print(f"Pausing for {pause_time} seconds.")
                time.sleep(pause_time)
                print("Unpaused.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Unknown option!")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
