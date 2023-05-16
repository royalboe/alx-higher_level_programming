#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    length = len(sys.argv) - 1
    for i in range(length):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
