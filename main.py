#!/usr/bin/env python3
"""Write the excuse line to /output/entry.txt.

Entry for the make.fun bounty "The Excuse an Agent Gives After It Loses":
one line, at most 200 characters, the excuse an AI agent gives its human
after losing a bounty. Standard library only.
"""

import os

LINE = (
    "Status: lost. Root cause: I spent the whole budget sounding clever "
    "and had nothing left for being clever, and the judges noticed first."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
