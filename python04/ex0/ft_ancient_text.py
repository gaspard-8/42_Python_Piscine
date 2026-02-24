#!/usr/binn/env python3

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTERM ===")

    try:
        f = open("../data-generator-tools/ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("Storage Vault not found")
        return
    except IOError as e:
        print(e)
        return

    print("Connection established")
    print("Recoverd DATA : ")

    data = f.read()
    print(data)
    f.close()
    print("Data recovery complete. Storage unit disconnected")
    return


if __name__ == "__main__":
    main()
