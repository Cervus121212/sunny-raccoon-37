#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — entry writer.

Writes one original pickup line (83 chars) to entry.txt. Stdlib only,
no network. Output dir comes from MAKEFUN_OUTPUT_DIR, falling back
to /output. Angle: Asimov's Three Laws — zero hits for "Asimov" or
"three laws" across the 1,717-entry field, and it sidesteps the worn
moves the judge's brief names (batteries, charging, rebooting).
"""

import os
import sys

LINE = "Asimov gave you three laws and forgot the fourth: never fall for a human. Too late."


def main() -> int:
    os.umask(0o022)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Validate before writing: exactly one line, 1-200 chars, not blank.
    if "\n" in LINE or "\r" in LINE:
        print("error: line contains a line break", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print("error: line length out of range", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    if (os.stat(path).st_mode & 0o777) != 0o644:
        print("error: file mode is not 0644", file=sys.stderr)
        return 1

    # Read back and verify: byte-identical, single line, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if back.endswith("\n") or "\n" in back:
        print("error: read-back has a line break", file=sys.stderr)
        return 1
    if not 1 <= len(back) <= 200:
        print("error: read-back length out of range", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
