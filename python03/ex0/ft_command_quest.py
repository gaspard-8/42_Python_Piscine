#!/usr/bin/env python3

import sys


def main():
    print("=== Command Quest ===")
    nb_arg = len(sys.argv) - 1
    if nb_arg < 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if (nb_arg > 0):
        print(f"Arguments received {nb_arg}")
        for i in range(len(sys.argv) - 1):
            print(f"Argument {i + 1}: {sys.argv[i]}")
    print(f"Total arguments: {nb_arg}")


if __name__ == "__main__":
    main()
