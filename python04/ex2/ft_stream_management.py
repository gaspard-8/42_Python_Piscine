#!/usr/binn/env python3

import sys


def main():
    print("=== CYBER ARCHIVES _ COMMUNICATION SYYSTEM ===")
    print()
    arch_id = input("Input stream active. Enter archivist ID:")
    status_report = input("Input stream active. Enter status report:")

    print(f"[STANDARD] Archive status from {arch_id} : {status_report}")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print("Three-channel communication test successful")

    return


if __name__ == "__main__":
    main()
