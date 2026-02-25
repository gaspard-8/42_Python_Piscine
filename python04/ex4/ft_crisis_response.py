#!/usr/bin/env python3

def access_archive(text: str) -> None:
    try:
        with open(text) as f:
            print(f"Archive recovered - '{f.read()}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintaned")
    else:
        print("STATUS: Normal operations resumed")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    access_archive("lost_archives")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    access_archive("classical_vault.txt")
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    access_archive("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")
    return


if __name__ == "__main__":
    main()
