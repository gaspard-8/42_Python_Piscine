#!/usr/bin/env python3

from typing import Generator
from timeit import default_timer as timer


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
        if evnt == "leveled up":
            lvl_event_count += 1
        if evnt == "killed monster":
            montser_killed += 1
        if evnt == "found treasure":
            tevent_count += 1
    print(f"Total events processed: {size}")
    print(f"High-level players (25+): {high_level_count}")
    print(f"Treasure events: {tevent_count}")
    print(f"Level-up events: {lvl_event_count}")
    print()


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c


def is_prime(a: int) -> bool:
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


def prime() -> Generator[int, None, None]:
    a = 2
    while True:
        yield a
        a += 1
        while (not is_prime(a)):
            a += 1


def main():
    print("=== Game data Stream Processor ===")
    print()
    nb_of_events = 500
    print(f"Processing {nb_of_events} events...")
    start = timer()
    game_event(nb_of_events)
    end = timer()
    time_taken = end - start
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {time_taken:.2} seconds")
    print()
    print("=== Generator Demonstration ===")
    fibo = fibonacci()
    prime_num = prime()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(9):
        print(next(fibo), end=", ")
    print((next(fibo)))
    print("Prime numbers (first 10): ", end="")
    for i in range(9):
        print(next(prime_num), end=", ")
    print((next(prime_num)))


if __name__ == "__main__":
    main()
