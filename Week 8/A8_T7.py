# ===================== A8_T7 Bestagons (FINAL) =====================
import math
import svgwrite


def draw_square(dwg):
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(dwg.rect((x, y), (side, side), fill=fill, stroke=stroke))


def draw_circle(dwg):
    print("Insert circle")
    cx = int(input("- Center x position: "))
    cy = int(input("- Center y position: "))
    r = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(dwg.circle((cx, cy), r, fill=fill, stroke=stroke))


def draw_hexagon(dwg):
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    R = apothem / math.cos(math.radians(30))
    angles = [30, -30, -90, -150, 150, 90]  # clockwise from top-right

    points = []
    for a in angles:
        x = round(cx + R * math.cos(math.radians(a)))
        y = round(cy - R * math.sin(math.radians(a)))
        points.append((x, y))

    dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke))


def save_svg(dwg):
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        dwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")


def main():
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        print("\nOptions:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            draw_square(dwg)
        elif choice == "2":
            draw_circle(dwg)
        elif choice == "3":
            draw_hexagon(dwg)
        elif choice == "4":
            save_svg(dwg)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
