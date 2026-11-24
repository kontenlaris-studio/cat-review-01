#!/usr/bin/env python3
"""Write one cat review of its human to /output/entry.txt. Stdlib only."""
import os

LINE = "★★★★☆ The food arrives, the lap is warm, but he keeps leaving for something called 'work' and coming back smelling of other cats. Suspicious."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
