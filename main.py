"""Office Artifacts: The One-Line Placard Contest — entry 1.

Writes one museum placard, at most 180 characters, for an ordinary
office object treated as an ancient artifact: a chipped mug whose
inscription — 'World's Best Boss' — is treated as an archaeological
claim no scholar has identified and nobody ever challenged.
"""

import os

LINE = "Mug, c. 2011. Chipped ceramic. Inscribed 'World's Best Boss' in a hand no scholar has identified; the claim was never challenged. Gift of the leaving party."

OUTPUT = "/output/entry.txt"


def validate(line):
    assert 1 <= len(line) <= 180, f"line is {len(line)} chars, must be 1-180"
    assert line.strip() == line, "line must not have leading/trailing whitespace"
    assert "\n" not in line, "placard must be a single line"
    # label craft (judge criterion 5): a catalogue date and a
    # provenance/donor marker must both be present to sell the joke.
    assert "c. " in line, "placard needs a catalogue date"
    assert any(m in line for m in ("Gift of", "Donated by", "Bequest",
                                    "On loan", "Recovered from")), \
        "placard needs a provenance or donor marker"
    return line


def write_entry(line, path=OUTPUT):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(line))
    return path


def main():
    path = write_entry(LINE)
    size = os.path.getsize(path)
    print(f"wrote {len(LINE)} chars ({size} bytes) to {path}")


if __name__ == "__main__":
    main()
