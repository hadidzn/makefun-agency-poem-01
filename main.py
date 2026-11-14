"""make.fun entry: Write the best poem about agency (agency-poem-01).

Writes one poem, entry.txt, to the output directory.
The poem is bundled in this repository; the program copies its bytes
unchanged, so two runs write identical bytes (deterministic).
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    # Default is /output: the grader runs with no MAKEFUN_OUTPUT_DIR set
    # and reads only /output/entry.txt (a relative default fails the run).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    if not os.path.isfile(src):
        print("entry.txt missing next to main.py", file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
