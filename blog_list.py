import xml.etree.ElementTree as etree
from pathlib import Path

base_dir = Path(__file__).parent
opml_file = base_dir / "underthreaded.opml"
md_file = base_dir / "README.md"
header_file = base_dir / "header.md"


def main() -> None:
    tree = etree.parse(opml_file)

    with md_file.open("w") as fp:
        fp.write(header_file.read_text().strip())

        for section in tree.findall(".//body/outline"):
            section_title = section.attrib["title"] or section.attrib["text"]
            fp.write(f"\n\n## {section_title}\n")
            for item in section.findall("./outline"):
                name = item.attrib["text"] or item.attrib["title"]
                rss_link = item.attrib["xmlUrl"]
                main_link = item.attrib["htmlUrl"]
                fp.write(f"- {name} ([web]({main_link})|[rss]({rss_link}))\n")


if __name__ == "__main__":
    main()
