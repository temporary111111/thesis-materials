"""Build a formatted Word draft from the reviewed Chapter 2 Markdown source.

This uses only the Python standard library so the research draft can be rebuilt
without installing Pandoc or python-docx.
"""

from __future__ import annotations

import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


SOURCE = Path("CHAPTER 2 - Review of Related Literature and Studies - Draft.md")
OUTPUT = Path("CHAPTER 2 - Review of Related Literature and Studies - AUDITED.docx")

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def run_xml(text: str, *, bold: bool = False, italic: bool = False) -> str:
    properties = []
    if bold:
        properties.append("<w:b/>")
    if italic:
        properties.append("<w:i/>")
    prop_xml = f"<w:rPr>{''.join(properties)}</w:rPr>" if properties else ""
    preserve = ' xml:space="preserve"' if text[:1].isspace() or text[-1:].isspace() else ""
    return f"<w:r>{prop_xml}<w:t{preserve}>{escape(text)}</w:t></w:r>"


def inline_xml(text: str) -> str:
    """Convert the small Markdown subset used in the manuscript to Word runs."""
    pieces = re.split(r"(\*\*.*?\*\*|(?<!\*)\*[^*]+?\*(?!\*))", text)
    output = []
    for piece in pieces:
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            output.append(run_xml(piece[2:-2], bold=True))
        elif piece.startswith("*") and piece.endswith("*"):
            output.append(run_xml(piece[1:-1], italic=True))
        else:
            output.append(run_xml(piece))
    return "".join(output)


def paragraph_xml(
    text: str,
    *,
    style: str = "Normal",
    page_break_before: bool = False,
    keep_with_next: bool = False,
) -> str:
    ppr = [f'<w:pStyle w:val="{style}"/>']
    if page_break_before:
        ppr.append("<w:pageBreakBefore/>")
    if keep_with_next:
        ppr.append("<w:keepNext/>")
    return f"<w:p><w:pPr>{''.join(ppr)}</w:pPr>{inline_xml(text)}</w:p>"


def table_xml(rows: list[list[str]]) -> str:
    widths = [2880, 4320, 4320]
    grid = "".join(f'<w:gridCol w:w="{width}"/>' for width in widths)
    table_rows = []
    for row_index, row in enumerate(rows):
        cells = []
        for column_index, value in enumerate(row):
            width = widths[min(column_index, len(widths) - 1)]
            shading = '<w:shd w:fill="D9EAF7"/>' if row_index == 0 else ""
            cell_props = (
                f'<w:tcW w:w="{width}" w:type="dxa"/>'
                f"{shading}<w:vAlign w:val=\"top\"/>"
            )
            run_content = run_xml(value, bold=True) if row_index == 0 else inline_xml(value)
            cell_paragraph = (
                '<w:p><w:pPr><w:pStyle w:val="TableText"/></w:pPr>'
                f"{run_content}</w:p>"
            )
            cells.append(f"<w:tc><w:tcPr>{cell_props}</w:tcPr>{cell_paragraph}</w:tc>")
        table_rows.append(f"<w:tr>{''.join(cells)}</w:tr>")

    properties = """
      <w:tblW w:w="0" w:type="auto"/>
      <w:tblLayout w:type="fixed"/>
      <w:tblBorders>
        <w:top w:val="single" w:sz="6" w:color="808080"/>
        <w:left w:val="single" w:sz="6" w:color="808080"/>
        <w:bottom w:val="single" w:sz="6" w:color="808080"/>
        <w:right w:val="single" w:sz="6" w:color="808080"/>
        <w:insideH w:val="single" w:sz="4" w:color="B7B7B7"/>
        <w:insideV w:val="single" w:sz="4" w:color="B7B7B7"/>
      </w:tblBorders>
    """
    return f"<w:tbl><w:tblPr>{properties}</w:tblPr><w:tblGrid>{grid}</w:tblGrid>{''.join(table_rows)}</w:tbl>"


def document_body(markdown: str) -> str:
    lines = markdown.splitlines()
    body = []
    index = 0
    in_references = False
    title_count = 0

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            index += 1
            continue

        if stripped.startswith("|"):
            table_rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                parts = [part.strip() for part in lines[index].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", part) for part in parts):
                    table_rows.append(parts)
                index += 1
            body.append(table_xml(table_rows))
            continue

        if stripped.startswith("### "):
            body.append(paragraph_xml(stripped[4:], style="Heading2", keep_with_next=True))
        elif stripped.startswith("## "):
            body.append(paragraph_xml(stripped[3:], style="Heading1", keep_with_next=True))
        elif stripped.startswith("# "):
            heading = stripped[2:]
            if heading == "References":
                in_references = True
                body.append(
                    paragraph_xml(
                        heading,
                        style="ReferenceHeading",
                        page_break_before=True,
                        keep_with_next=True,
                    )
                )
            else:
                title_count += 1
                body.append(
                    paragraph_xml(
                        heading,
                        style="ChapterTitle",
                        page_break_before=title_count == 1,
                        keep_with_next=True,
                    )
                )
        elif in_references:
            body.append(paragraph_xml(stripped, style="Reference"))
        elif stripped.startswith("**Figure ") or (
            stripped.startswith("**Input") and stripped.endswith("**")
        ):
            body.append(paragraph_xml(stripped, style="Caption", keep_with_next=True))
        else:
            body.append(paragraph_xml(stripped))
        index += 1

    section = """
      <w:sectPr>
        <w:pgSz w:w="12240" w:h="15840"/>
        <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"
                 w:header="720" w:footer="720" w:gutter="0"/>
        <w:cols w:space="720"/>
        <w:docGrid w:linePitch="360"/>
      </w:sectPr>
    """
    return "".join(body) + section


STYLES_XML = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
  <w:docDefaults>
    <w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-US"/></w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="480" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/><w:qFormat/>
    <w:pPr><w:spacing w:after="0" w:line="480" w:lineRule="auto"/><w:ind w:firstLine="720"/><w:jc w:val="both"/></w:pPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ChapterTitle">
    <w:name w:val="Chapter Title"/><w:basedOn w:val="Normal"/><w:qFormat/>
    <w:pPr><w:spacing w:before="0" w:after="240" w:line="480" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="Heading 1"/><w:basedOn w:val="Normal"/><w:qFormat/>
    <w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="120" w:line="480" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:jc w:val="left"/><w:outlineLvl w:val="0"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="Heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/>
    <w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="180" w:after="60" w:line="480" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:jc w:val="left"/><w:outlineLvl w:val="1"/></w:pPr>
    <w:rPr><w:b/><w:i/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Caption">
    <w:name w:val="Caption"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:keepNext/><w:spacing w:before="120" w:after="60" w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="TableText">
    <w:name w:val="Table Text"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ReferenceHeading">
    <w:name w:val="Reference Heading"/><w:basedOn w:val="ChapterTitle"/><w:qFormat/>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Reference">
    <w:name w:val="Reference"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:after="0" w:line="480" w:lineRule="auto"/><w:ind w:left="720" w:hanging="720"/><w:jc w:val="left"/></w:pPr>
  </w:style>
</w:styles>'''


CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

PACKAGE_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

DOCUMENT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>'''

SETTINGS_XML = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="{W}"><w:zoom w:percent="100"/><w:defaultTabStop w:val="720"/><w:compat/></w:settings>'''

APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Codex Chapter 2 Builder</Application></Properties>'''


def main() -> None:
    markdown = SOURCE.read_text(encoding="utf-8")
    body = document_body(markdown)
    document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W}"><w:body>{body}</w:body></w:document>'''

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    core_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Chapter 2 - Review of Related Literature and Studies</dc:title><dc:subject>Machine Learning Classification of AI-Generated and Real Text-Containing Images Using Visual Text-Region Features</dc:subject><dc:creator>Research draft</dc:creator><cp:lastModifiedBy>Codex</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:modified></cp:coreProperties>'''

    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", CONTENT_TYPES)
        archive.writestr("_rels/.rels", PACKAGE_RELS)
        archive.writestr("docProps/core.xml", core_xml)
        archive.writestr("docProps/app.xml", APP_XML)
        archive.writestr("word/document.xml", document_xml)
        archive.writestr("word/styles.xml", STYLES_XML)
        archive.writestr("word/settings.xml", SETTINGS_XML)
        archive.writestr("word/_rels/document.xml.rels", DOCUMENT_RELS)

    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
