#!/usr/bin/env python3

def access_archive(text: str) -> None:
    print("CRISIS ALERT")
    try:
        with open(text) as f:
            print("Vault connection established with failsafe protocol")
            print(f"")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintaned")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    access_archive("lost_archives")
    return


if __name__ == "__main__":
    main()
