#!/usr/bin/env python3

def main():

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    with open("../data-generator-tools/classified_data.txt") as f:
        print("Vault connection established with failsafe protocol")
        text = f.read()
        print(text)
    print()

    print("SECURE PRESERVATION")
    with open("../data-generator-tools/security_protocols.txt") as f:
        print(f.read())
    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")
    return


if __name__ == "__main__":
    main()
