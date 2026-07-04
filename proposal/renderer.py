from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape,
)

BASE_DIR = Path(__file__).resolve().parent.parent


class HtmlRenderer:

    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader(BASE_DIR / "templates"),
            autoescape=select_autoescape(["html"]),
        )

    def render(self, context: dict) -> str:
        
        context["logo_svg"] = (
            BASE_DIR / "assets/logo.svg"
        ).read_text(encoding="utf-8")

        context["inline_css"] = (
            BASE_DIR / "css" / "proposal.css"
        ).read_text(encoding="utf-8")

        template = self.env.get_template("proposal.html")

        return template.render(**context)

    def save(self, html: str) -> Path:

        output = BASE_DIR / "output"
        output.mkdir(parents=True, exist_ok=True)

        html_file = output / "proposal.html"

        html_file.write_text(
            html,
            encoding="utf-8",
        )

        return html_file