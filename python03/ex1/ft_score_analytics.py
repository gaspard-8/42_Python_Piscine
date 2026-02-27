#!/usr/bin/env python3

import sys


def main():
    print("=== Player Score Analytics ===")
    scores = []
    for score in (sys.argv[1:]):
        try:
            int_score = int(score)
            scores.append(int_score)
        except (ValueError, TypeError):
            print(f"Invalid score '{score}' will be ignored")
    if (len(scores) == 0):
        print("No scores provided. Usage : python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return
    print(f"scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"High score : {max(scores)}")
    print(f"Low score {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
