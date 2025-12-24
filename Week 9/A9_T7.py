# A9_T7.py


import os
import sys

def show_help() -> None:
    print("Synopsis:")
    print("  python {} <src_file> <dst_file>".format(os.path.basename(sys.argv[0])))

def copy_file(src: str, dst: str) -> None:
    proceed = True

    if os.path.exists(dst):
        ans = input("Destination file exists. Overwrite(y/n)?: ").strip().lower()
        proceed = (ans == "y")

    if not proceed:
        return

    try:
        with open(src, "r", encoding="utf-8") as fsrc:
            data = fsrc.read()
        with open(dst, "w", encoding="utf-8") as fdst:
            fdst.write(data)
    except Exception as e:
        print("Error! {}".format(e))
        sys.exit(-1)

def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        show_help()
        print("Program ending.")
        return

    src = sys.argv[1]
    dst = sys.argv[2]

    print('Source file "{}"'.format(src))
    print('Destination file "{}"'.format(dst))
    print('Copying file "{}" to "{}".'.format(src, dst))

    copy_file(src, dst)

    print("Program ending.")


if __name__ == "__main__":
    main()
