# A10_T7 Minesweeper field

import random

random.seed(1234)


def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows else 0
    total = rows * cols
    mines = min(PMines, total)

    # pick unique positions
    positions = random.sample(range(total), mines)
    for pos in positions:
        r = pos // cols
        c = pos % cols
        PMineField[r][c] = 9

    return None


def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows else 0

    def count_adjacent_mines(r: int, c: int) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and PMineField[rr][cc] == 9:
                    count += 1
        return count

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] != 9:
                PMineField[r][c] = count_adjacent_mines(r, c)

    return None


def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    PMineField.clear()

    for _ in range(PRows):
        PMineField.append([0] * PCols)

    layMines(PMineField, PMines)
    calculateNearbys(PMineField)
    return None


def show_board(board: list[list[int]]) -> None:
    if not board:
        print("(empty)")
        return
    for row in board:
        print(" ".join(str(x) for x in row))


def save_board_csv(board: list[list[int]], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for row in board:
            f.write(",".join(str(x) for x in row) + "\n")


def main() -> None:
    print("Program starting.")
    board: list[list[int]] = []
    saved_name = ""

    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(board, rows, cols, mines)
            print("Board generated.")

        elif choice == "2":
            show_board(board)

        elif choice == "3":
            if not board:
                print("Generate a board first.")
                continue
            saved_name = input("Insert save filename: ").strip()
            save_board_csv(board, saved_name)
            print(f"Saved: {saved_name}")

        elif choice == "0":
            print("Program ending.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
