from pathlib import Path
import base64

from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape,
)

BASE_DIR = Path(__file__).resolve().parent.parent


def asset_data_uri(path: Path, mime_type: str) -> str:
    return (
        f"data:{mime_type};base64,"
        + base64.b64encode(
            path.read_bytes()
        ).decode()
    )


class HtmlRenderer:

    def __init__(self):

        self.env = Environment(
            loader=FileSystemLoader(
                BASE_DIR / "templates"
            ),
            autoescape=select_autoescape(
                enabled_extensions=("html",),
                default_for_string=False,
                default=False,
            ),
        )

    def render(self, context: dict) -> str:

        logo = BASE_DIR / "assets" / "logo.png"
        signature = BASE_DIR / "assets" / "signature.jpeg"
        client_logo = BASE_DIR / "assets" / "sibl-logo.png"

        context["logo"] = asset_data_uri(
            logo,
            "image/png",
        )

        context["signature"] = asset_data_uri(
            signature,
            "image/jpeg",
        )

        if client_logo.exists():
            context["client"]["logo"] = asset_data_uri(
                client_logo,
                "image/png",
            )

        context["inline_css"] = (
            BASE_DIR
            / "css"
            / "proposal.css"
        ).read_text(
            encoding="utf-8"
        )

        template = self.env.get_template(
            "proposal.html"
        )

        return template.render(
            **context
        )

    def save(
        self,
        html: str,
    ) -> Path:

        output = BASE_DIR / "output"

        output.mkdir(
            parents=True,
            exist_ok=True,
        )

        html_file = output / "proposal.html"

        html_file.write_text(
            html,
            encoding="utf-8",
        )

        return html_file
