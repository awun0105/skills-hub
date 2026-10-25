#!/usr/bin/env python3
"""Check README / docs files filled from the Best-Readme-Template templates.

    check_readme.py README.md README_VN.md [docs/ ...]

Reports, per file:
  - leftover template parts: [bracketed placeholders], [MANDATORY] / [BẮT BUỘC] /
    [OPTIONAL] / [TÙY CHỌN] markers, instruction comment blocks, *italic notes*
  - table-of-contents / in-page links (#anchor) that match no heading (GitHub slugs)
  - relative links and images pointing to files that don't exist
  - emoji in headings (the templates are icon-free)
and, for each EN/VN pair given, whether both have the same number of ## sections.
Exit code 1 when a problem is found.
"""
import re
import sys
import unicodedata
from pathlib import Path

MARKERS = re.compile(r"\[(MANDATORY|OPTIONAL|RECOMMENDED|BẮT BUỘC|TÙY CHỌN|KHUYẾN NGHỊ)[^\]]*\]", re.I)
COMMENT_HINT = re.compile(r"AGENT EXECUTION PROTOCOL|GIAO THỨC THỰC THI|UNIVERSAL README TEMPLATE|BẢN MẪU README|DOCUMENTATION TEMPLATE|BẢN MẪU TÀI LIỆU", re.I)
PLACEHOLDER = re.compile(r"(?<![!\]])\[(?![ xX]\])(?!!)[^\]\n]{2,}\](?![(\[:])")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_LINK = re.compile(r"(?:href|src)=\"([^\"]+)\"")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def slug(text, seen):
    """GitHub's heading anchor: lower-case, drop punctuation, spaces → '-'."""
    t = re.sub(r"<[^>]+>", "", text)
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("`", "").strip().lower()
    t = "".join(c for c in t if c in " -_" or unicodedata.category(c)[0] in "LNM")
    t = t.replace(" ", "-")
    n = seen.get(t, 0)
    seen[t] = n + 1
    return t if n == 0 else f"{t}-{n}"


def prose_lines(text):
    fence = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith(("```", "~~~")):
            fence = not fence
            continue
        if not fence:
            yield n, re.sub(r"`[^`]*`", "", line)


def check(path):
    text = path.read_text(encoding="utf-8")
    problems = []
    seen, anchors = {}, set()
    for _, line in prose_lines(text):
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m:
            anchors.add(slug(m.group(2), seen))
            if EMOJI.search(m.group(2)):
                problems.append(f"emoji in heading: {m.group(2)}")
    anchors |= set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    if COMMENT_HINT.search(text):
        problems.append("template instruction block still present")
    for n, line in prose_lines(text):
        if MARKERS.search(line):
            problems.append(f"line {n}: template marker {MARKERS.search(line).group(0)}")
        for ph in PLACEHOLDER.findall(line):
            problems.append(f"line {n}: placeholder left? {ph}")
        if re.match(r"^\s*\*[^*\s].*[^*\s]\*\s*$", line):
            problems.append(f"line {n}: italic instruction note left? {line.strip()[:80]}")
        for target in LINK.findall(line) + HTML_LINK.findall(line):
            if re.match(r"^[a-z][\w+.-]*:", target) or target.startswith("//"):
                continue
            file_part, _, frag = target.partition("#")
            if not file_part:
                if frag and frag not in anchors:
                    problems.append(f"line {n}: no heading for #{frag}")
                continue
            if not (path.parent / file_part).exists():
                problems.append(f"line {n}: missing file {file_part}")
    sections = sum(1 for _, l in prose_lines(text) if re.match(r"^##\s", l))
    return problems, sections


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__.strip())
        return 2
    paths = []
    for a in args:
        p = Path(a)
        paths += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    bad = 0
    counts = {}
    for p in paths:
        problems, sections = check(p)
        counts[p] = sections
        for pr in problems:
            print(f"{p}: {pr}")
        bad += len(problems)
    # EN / VN pairs: README.md ↔ README_VN.md (or README.en.md ↔ README.md), docs/EN/x ↔ docs/VN/x
    for p in paths:
        s = str(p)
        for a, b in (("README.md", "README_VN.md"), ("README.en.md", "README.md"), ("/EN/", "/VN/")):
            if a in s:
                q = Path(s.replace(a, b))
                if q in counts and q != p and counts[q] != counts[p]:
                    print(f"{p} has {counts[p]} sections, {q} has {counts[q]}")
                    bad += 1
    print(f"{bad} problem(s)" if bad else "README check passed.", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
