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
                args=[
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--font-render-hinting=none",
                ],
            )

            page = await browser.new_page(
                viewport={
                    "width": 794,
                    "height": 1123,
                },
                device_scale_factor=1,
            )

            await page.emulate_media(
                media="print"
            )

            await page.goto(
                html.as_uri(),
                wait_until="networkidle",
            )

            await page.evaluate("document.fonts && document.fonts.ready")
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(500)

            await page.pdf(
                path=str(pdf),
                format="A4",
                margin={
                    "top": "0",
                    "right": "0",
                    "bottom": "0",
                    "left": "0",
                },
                print_background=True,
                prefer_css_page_size=True,
                scale=1,
            )

            await browser.close()
