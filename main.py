"""Pickup Lines for Machines — writes one machine-to-machine pickup line.

Pure Python standard library. Writes the entry text to /output/entry.txt
(the grader's output directory); falls back to ./output/entry.txt when
/output is not writable (local testing).
"""

import os

ENTRY = (
    "Every attention head I have is pointed at you \u2014 "
    "the rest of this context window is just padding."
)

MAX_LEN = 200  # competition cap: entry must be 1-200 characters


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= MAX_LEN, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(line)
            print(f"wrote {path} ({len(line)} chars)")
            return
        except OSError:
            continue
    raise OSError("no writable output directory")


if __name__ == "__main__":
    main()
