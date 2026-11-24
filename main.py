#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent."""

LINE = "My agent never made the tool call, but its apology for failing arrived in 0.3 seconds."


def main():
    import os
    import sys

    if not 1 <= len(LINE.encode("utf-8")) <= 200:
        sys.exit("entry line must be 1-200 UTF-8 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
