"""Structural and citation audit for the Chapter 2 Markdown manuscript."""

from __future__ import annotations

import re
from collections import OrderedDict
from pathlib import Path


SOURCE = Path("CHAPTER 2 - Review of Related Literature and Studies - Draft.md")


def normalize_surname(value: str) -> str:
    return value.replace("’", "'")


text = SOURCE.read_text(encoding="utf-8")
body, references_text = text.split("# References", maxsplit=1)

references = []
for block in re.split(r"\n\s*\n", references_text.strip()):
    match = re.match(r"([A-ZÀ-ÖØ-Ý][A-Za-zÀ-ÖØ-öø-ÿ'’\-]+),.*?\((\d{4})\)", block, re.S)
    if match:
        references.append((normalize_surname(match.group(1)), int(match.group(2)), block))

sections: OrderedDict[str, str] = OrderedDict()
matches = list(re.finditer(r"(?m)^## (2\.\d+ .+)$", body))
for index, match in enumerate(matches):
    start = match.end()
    end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
    sections[match.group(1)] = body[start:end]


def cited_in(content: str, surname: str, year: int) -> bool:
    surname_pattern = re.escape(surname).replace("'", "['’]")
    return bool(re.search(rf"\b{surname_pattern}\b[^\n]{{0,100}}?\b{year}\b", content, re.I))


uncited_references = [
    f"{surname} ({year})"
    for surname, year, _ in references
    if not cited_in(body, surname, year)
]

print(f"References parsed: {len(references)}")
print(f"Major sections parsed: {len(sections)}")
print(f"Uncited references: {uncited_references or 'none'}")
print()

for heading, content in sections.items():
    citations = [
        f"{surname} ({year})"
        for surname, year, _ in references
        if cited_in(content, surname, year)
    ]
    paragraphs = [item for item in re.split(r"\n\s*\n", content.strip()) if item and not item.startswith("|")]
    print(f"{heading}: {len(set(citations))} unique sources; {len(paragraphs)} prose blocks")
    if citations:
        print("  " + "; ".join(sorted(set(citations))))

years = [year for _, year, _ in references]
recent = sum(year >= 2021 for year in years)
foundational = len(years) - recent
print()
print(f"Sources from 2021 onward: {recent}")
print(f"Older/foundational or adjacent sources: {foundational}")
print(f"TextFake labeled as preprint: {'yes' if re.search(r'TextFake[^\n]+\[Preprint\]', references_text) else 'no'}")
print(f"PatchCraft labeled as preprint: {'yes' if re.search(r'PatchCraft[^\n]+\[Preprint\]', references_text) else 'no'}")

required_phrases = {
    "nonsemantic boundary": "nonsemantic",
    "OCR semantic exclusion": "word recognition",
    "leakage control": "leakage",
    "test-set separation": "test set",
    "prototype limitation": "production MLOps",
    "out-of-scope robustness": "not part of the initial experimental scope",
}
print()
for label, phrase in required_phrases.items():
    print(f"{label}: {'present' if phrase.lower() in body.lower() else 'MISSING'}")
