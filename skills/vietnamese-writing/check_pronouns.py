#!/usr/bin/env python3
"""List personal pronouns (tôi, bạn, chúng ta, mình…) in Vietnamese text.

    check_pronouns.py FILE_OR_DIR [...]      # .md, .txt, .html, .mdx files

Skips fenced code blocks, inline `code` and HTML comments. Prints
file:line: text with the hits marked [like this]; exit code 1 when anything
is found. Review each hit: a few words have non-pronoun meanings.
"""
import re
import sys
from pathlib import Path

# Longer forms first so "chúng tôi" wins over "tôi".
PRONOUNS = [
    "chúng tôi", "chúng ta", "chúng mình", "chúng tớ", "các bạn", "quý vị", "quý khách", "bọn mình",
    "tôi", "tớ", "ta", "mình", "bạn", "cậu", "anh", "chị", "em", "họ", "nó",
]
# Phrases where the word is not a pronoun.
ALLOW = [
    "họ tên", "họ và tên", "dòng họ", "anh hùng", "tiếng anh", "nước anh", "người anh",
    "bạn bè" , "bạn đồng hành", "ta-",
]
WORD = re.compile(r"(?<![\w])(" + "|".join(re.escape(p) for p in PRONOUNS) + r")(?![\w])", re.IGNORECASE)
EXTS = {".md", ".mdx", ".txt", ".html", ".htm"}


def files(args):
    for a in args:
        p = Path(a)
        if p.is_dir():
            yield from (f for f in sorted(p.rglob("*")) if f.suffix.lower() in EXTS and ".git" not in f.parts and "node_modules" not in f.parts)
        elif p.exists():
            yield p


def scan(path):
    hits = []
    fence = False
    comment = False
    blank = lambda m: " " * len(m.group())
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        if fence:
            continue
        # Blank out (same length) what isn't prose, so hit positions match the original line.
        text = line
        if comment:
            end = text.find("-->")
            if end < 0:
                continue
            text = " " * (end + 3) + text[end + 3:]
            comment = False
        text = re.sub(r"<!--.*?-->", blank, text)
        start = text.find("<!--")
        if start >= 0:
            text = text[:start] + " " * (len(text) - start)
            comment = True
        text = re.sub(r"`[^`]*`", blank, text)
        low = text.lower()
        for a in ALLOW:
            low = low.replace(a, " " * len(a))
        found = list(WORD.finditer(low))
        if found:
            marked = line
            for m in reversed(found):
                marked = marked[:m.start()] + "[" + marked[m.start():m.end()] + "]" + marked[m.end():]
            hits.append((n, marked.strip()))
    return hits


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    total = 0
    for f in files(sys.argv[1:]):
        for n, t in scan(f):
            print(f"{f}:{n}: {t}")
            total += 1
    print(f"{total} line(s) with pronouns" if total else "No personal pronouns found.", file=sys.stderr)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
