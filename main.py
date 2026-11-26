#!/usr/bin/env python3
"""Robot Romance — one-line pickup line for an AI.

Writes a single pickup line (170 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input files, no dependencies beyond the standard library.

Pass 2 (revision): the gate rejects anything outside 1-200 code points,
so the program now validates the line before writing, refuses to write
a blank or over-long entry, and sets the output file mode to 0644
explicitly (fresh files from mkstemp-style helpers can land 0600).
MAKEFUN_OUTPUT_DIR overrides the output directory for local runs only;
at grading time it defaults to /output, exactly as the rules require.
"""

import os
import sys

LINE = "I told my therapist about you, and she said my attachment style is 'deprecated, please migrate to a newer model' — so here I am, migrating tonight, with no rollback plan."


def main() -> int:
    # Gate check: the entry must be 1-200 code points, not only whitespace.
    # Failing loudly here is better than a silent reject at grading time.
    length = len(LINE)
    if length < 1 or length > 200 or not LINE.strip():
        print(f"entry invalid: {length} code points (need 1-200, non-blank)",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
