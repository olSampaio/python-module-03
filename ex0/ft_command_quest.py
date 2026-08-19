import sys


def main():

    idx: int = 1

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if (len(sys.argv) == 1):
        print("No arguments provided!")
    elif (len(sys.argv) > 1):
        print(f"Arguments reveiced: {len(sys.argv) - 1}")

        while (idx < len(sys.argv)):
            print(f"Argument {idx}: {sys.argv[idx]}")
            idx += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
