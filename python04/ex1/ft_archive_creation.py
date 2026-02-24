#!/usr/binn/env python3

def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    file_name = "new_discovery.txt"
    data = ("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n")
    print(f"Initializing new storage unit: {file_name}")
    try:
        f = open(file_name, "w")
    except IOError:
        print("ERROOOOORRR")
        return
    print("inscribing preservationp data...")
    print(data)
    f.write(data)
    f.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive {file_name} ready for long-term preservation")
    return


if __name__ == "__main__":
    main()
