# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A single-file static brochure for the VibeDent dental clinic, published at [alimuradov.github.io/vibedent-buklet](https://alimuradov.github.io/vibedent-buklet/). All source, styling, copy, and embedded assets live in `index.html`. There is no build step or package manager.

## Commands

```bash
# Local preview
python3 -m http.server 8000
xdg-open http://localhost:8000   # Linux

# Export PDF (requires playwright + google-chrome)
python3 scripts/export_pdf.py

# Pre-commit check
git diff --check
```

`export_pdf.py` spins up a local HTTP server on a random port, loads the page with `?export=1` appended (which sets `html.export-mode` via JS), then uses Playwright/Chromium to print to A4 landscape PDF with zero margins.

## Architecture

`index.html` is the entire source. It uses Tailwind CSS (CDN) with a custom config block at the top that defines the brand palette (`teal`, `coral`, `dark`, etc.).

Layout is two A4 landscape sheets (`297mm × 210mm`), each divided into three `99mm` panels:

- **Sheet 1 (outside):** `.p1` cover, `.p2` intro/pain points, `.p3` services
- **Sheet 2 (inside):** `.p4` technology/team, `.p5` results/testimonials, `.p6` contact/CTA

Key structural classes:
- `.sheet` — one A4 landscape page wrapper
- `.panel` — a 99mm-wide column within a sheet
- `.label` / `.sheet-label` — print-hidden UI labels (hidden in `export-mode`)
- `.export-button` — also hidden in export

QR codes and decorative illustrations are embedded inline as SVG or base64.

## Print/export notes

The `?export=1` query param triggers `export-mode` class on `<html>`, which removes shadows, margins, and UI elements so the PDF renders cleanly. `prefer_css_page_size: true` is set in the Playwright call so `@page { size: A4 landscape; }` controls pagination.

After layout changes, verify in browser print preview that panel widths and page breaks remain intact.

## Style conventions

- 2-space indentation throughout HTML and CSS
- All styles live inside the single `<style>` block in `<head>`
- Class names are panel-scoped: `.p6-head`, `.pain-card`, `.cover-glass`, etc.
- Copy is in Russian; preserve tone and marketing voice

## Commit style

Short imperative subjects scoped to one visual/content change: `Update CTA copy`, `Refine panel spacing`, `Add cover photo`. PRs should note before/after and any print checks performed.
