#!/usr/bin/env python3

# from typing import Generator


def cycle(iterate: list):
    while True:
        for thing in iterate:
            yield thing


def game_event(size: int):
    players = cycle(["alice", "bob", "charlie", "madonna", "beyonce"])
    level = cycle([((i + ((i**3) % 7)) % 50) for i in range(1000)])
    event = cycle(["leveled up", "killed monster", "found treasure"])
    high_level_count = 0
    tevent_count = 0
    lvl_event_count = 0
    montser_killed = 0
    for i in range(size):
        lvl = next(level)
        player = next(players)
        evnt = next(event)
        print(f"{player} (level {lvl}) {evnt}")
        if lvl > 25:
            high_level_count += 1
        if event == "leveled up":
            lvl_event_count += 1
        if event == "killed monster":
            montser_killed += 1
        if event == "found treasure":
            tevent_count += 1
    print(f"Total events processed: {size}")
    print(f"High-level players (25+): {high_level_count}")
    print(f"Treasure events: {tevent_count}")
    print(f"Level-up events: {}")


def main():
    print("=== Game data Stream Processor ===")
    print()
    nb_of_events = 500
    print(f"Processing {nb_of_events} events...")
    game_event(nb_of_events)

    print("=== Stream analytics ===")
    print(f"Total events processed : {nb_of_events}")


if __name__ == "__main__":
    main()
