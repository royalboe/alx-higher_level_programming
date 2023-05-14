#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    print("{} arguments.".format(count) if count != 1 else "1 argument:")
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
