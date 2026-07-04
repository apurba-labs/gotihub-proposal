import json
import asyncio
from pathlib import Path

from proposal.models import ProposalData
from proposal.renderer import HtmlRenderer
from proposal.pdf import PdfGenerator

BASE_DIR = Path(__file__).resolve().parent.parent


class ProposalGenerator:

    def build(self):

        proposal_file = BASE_DIR / "data" / "proposal.json"
        with proposal_file.open(
            encoding="utf-8"
        ) as f:

            data = ProposalData.model_validate(
                json.load(f)
            )

        renderer = HtmlRenderer()

        html = renderer.render(
            data.model_dump()
        )

        renderer.save(html)

        #asyncio.run(
        #    PdfGenerator().generate()
        #)