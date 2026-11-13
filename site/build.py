"""Build the public FEmbussy page from the multilingual README."""
from html import escape
from pathlib import Path
import re
import shutil
import sys

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = Path(sys.argv[1]).resolve()
REPO = "https://github.com/geovannec/LTD_Fembussy"
LANGUAGES = (
    ("English", "en"), ("Русский", "ru"), ("한국어", "ko"),
    ("Português", "pt-BR"), ("Español", "es"), ("Français", "fr"),
)

readme = (ROOT / "README.md").read_text(encoding="utf-8")
translation_text, references = readme.split("\n---\n", 1)
references = references[references.index("[download]:"):]
references = re.sub(r"(: )([A-Z][A-Z]+\.md)$", rf"\1{REPO}/blob/main/\2", references, flags=re.M)
parts = re.split(r"^## (.+)$", translation_text, flags=re.M)[1:]
sections = dict(zip(parts[::2], parts[1::2]))
if tuple(sections) != tuple(name for name, _ in LANGUAGES):
    raise ValueError("README language headings must match the site navigation.")

navigation = []
articles = []
for name, code in LANGUAGES:
    navigation.append(f'<a href="#{code}" lang="{code}">{escape(name)}</a>')
    body = markdown.markdown(sections[name] + "\n\n" + references)
    articles.append(
        f'<article id="{code}" lang="{code}"><h2>{escape(name)}</h2>{body}</article>'
    )

template = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
OUTPUT.mkdir(parents=True, exist_ok=True)
(OUTPUT / "index.html").write_text(
    template.replace("<!-- languages -->", " ".join(navigation))
    .replace("<!-- articles -->", "\n".join(articles)),
    encoding="utf-8",
)
shutil.copyfile(ROOT / "site" / "style.css", OUTPUT / "style.css")
shutil.copyfile(ROOT / "assets" / "fembussy-crest.png", OUTPUT / "crest.png")
