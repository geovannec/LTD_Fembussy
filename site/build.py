"""Build the public LTDCE page from the multilingual README."""
from html import escape
from pathlib import Path
import re
import shutil
import sys

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = Path(sys.argv[1]).resolve()
REPO = "https://github.com/ltdce/LTDCE"
LANGUAGES = (
    ("English", "en"), ("Русский", "ru"), ("한국어", "ko"),
    ("Português", "pt-BR"), ("Español", "es"), ("Français", "fr"),
)

def render_page(filename, template_name, first_reference, output_name):
    source = (ROOT / filename).read_text(encoding="utf-8")
    content, references = source.split(f"\n[{first_reference}]:", 1)
    references = f"[{first_reference}]:" + references
    references = re.sub(
        r"(: )(DIFFERENCES|HISTORIA)\.md$", rf"\1{REPO}/blob/main/\2.md",
        references, flags=re.M,
    )
    translation_text = content.split("\n---\n", 1)[0]
    parts = re.split(r"^## (.+)$", translation_text, flags=re.M)[1:]
    sections = dict(zip(parts[::2], parts[1::2]))
    if tuple(sections) != tuple(name for name, _ in LANGUAGES):
        raise ValueError(f"{filename} language headings must match the site navigation.")

    navigation = []
    articles = []
    for name, code in LANGUAGES:
        navigation.append(f'<a href="#{code}" lang="{code}">{escape(name)}</a>')
        localized_references = re.sub(r"COMMUNITY\.md#[^\n]+", f"voting.html#{code}", references)
        body = markdown.markdown(sections[name] + "\n\n" + localized_references)
        articles.append(f'<article id="{code}" lang="{code}"><h2>{escape(name)}</h2>{body}</article>')

    template = (ROOT / "site" / template_name).read_text(encoding="utf-8")
    (OUTPUT / output_name).write_text(
        template.replace("<!-- languages -->", " ".join(navigation))
        .replace("<!-- articles -->", "\n".join(articles)),
        encoding="utf-8",
    )

OUTPUT.mkdir(parents=True, exist_ok=True)
render_page("README.md", "index.html", "download", "index.html")
render_page("COMMUNITY.md", "voting.html", "ideas", "voting.html")
shutil.copyfile(ROOT / "site" / "style.css", OUTPUT / "style.css")
shutil.copyfile(ROOT / "assets" / "ltdce-crest.png", OUTPUT / "crest.png")
