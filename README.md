# GOTIHUB Proposal Generator

A professional proposal generation system built with Python, Jinja2, and Playwright.

The project generates branded HTML and PDF business proposals from structured JSON data, making it easy to create consistent, client-ready documents.

---

## Features

- JSON-driven proposal generation
- Jinja2 template engine
- Reusable HTML page components
- Inline CSS rendering
- Base64 embedded assets
- Professional A4 layout
- Playwright PDF generation
- Corporate branding support
- Modular template architecture

---

## Project Structure

```text
.
├── assets/
│   ├── logo.png
│   └── ...
├── css/
│   └── proposal.css
├── data/
│   └── proposal.json
├── output/
│   ├── proposal.html
│   └── proposal.pdf
├── proposal/
│   ├── generator.py
│   ├── renderer.py
│   ├── pdf.py
│   └── models.py
├── templates/
│   ├── proposal.html
│   ├── cover.html
│   ├── letter.html
│   ├── company.html
│   ├── requirements.html
│   ├── scope.html
│   ├── technology.html
│   ├── timeline.html
│   ├── commercial.html
│   ├── support.html
│   └── thankyou.html
└── main.py
```

---

## Installation

```bash
git clone <repository>

cd gotihub-proposal

uv sync
```

Install Playwright browser:

```bash
playwright install chromium
```

---

## Usage

Generate proposal:

```bash
uv run python main.py
```

Generated files:

```
output/proposal.html
output/proposal.pdf
```

---

## Technology Stack

- Python
- Jinja2
- Pydantic
- Playwright
- HTML5
- CSS3

---

## Configuration

Proposal content is stored in:

```
data/proposal.json
```

Update the JSON file to generate proposals for different clients without modifying templates.

---

## Current Status

- HTML generation ✅
- Modular templates ✅
- Corporate proposal layout ✅
- JSON data model ✅
- PDF generation ✅
- Branding support ✅

---

## Roadmap

- Multiple proposal themes
- Digital signature support
- DOCX export
- Email delivery
- Multi-language templates
- Charts and financial tables
- Dynamic pricing modules

---

## License

MIT License

---

Built with ❤️ by GOTIHUB

Enterprise Software Engineering & Digital Transformation