
import svgwrite


def draw_square(dwg: svgwrite.Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(dwg.rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))


def draw_circle(dwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center x position: "))
    cy = int(input("- Center y position: "))
    r = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(dwg.circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))


def save_svg(dwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        dwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")


def main() -> None:
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        print("\nOptions:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            draw_square(dwg)
        elif choice == "2":
            draw_circle(dwg)
        elif choice == "3":
            save_svg(dwg)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
