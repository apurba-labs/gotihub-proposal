from pathlib import Path

from playwright.async_api import async_playwright


BASE_DIR = Path(__file__).resolve().parent.parent


class PdfGenerator:

    async def generate(self):

        html = (
            BASE_DIR
            / "output"
            / "proposal.html"
        ).resolve()

        pdf = (
            BASE_DIR
            / "output"
            / "proposal.pdf"
        )

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox"],
            )

            page = await browser.new_page()

            await page.goto(
                html.as_uri(),
                wait_until="load",
            )

            # wait for fonts/css

            await page.wait_for_timeout(1000)

            await page.pdf(
                path=str(pdf),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
            )

            await browser.close()