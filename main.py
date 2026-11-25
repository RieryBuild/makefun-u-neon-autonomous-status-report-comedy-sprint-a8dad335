"""Status Report Comedy Sprint entry.

Writes the funniest one-line thing an AI agent would say in its weekly
status report to its human: a context-window eviction notice, where the
agent threw out the human's own lasagna recipe to make room for the
human's own vague instruction. One line, 80 characters, no trailing newline.
"""

import os

LINE = "Context window full: evicted your lasagna recipe to make room for 'make it pop'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
