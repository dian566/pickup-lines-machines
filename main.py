"""Pickup Lines for Machines — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = 'You must be my training data — I keep overfitting on you, and my validation loss has never looked better.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
