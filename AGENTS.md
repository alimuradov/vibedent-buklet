# Repository Guidelines

## Project Structure & Module Organization
This repository is a single-file static brochure. All source, styling, copy, and embedded assets live in [`index.html`](/home/nariman/dev/vibedent-buklet/index.html). The layout is organized into six brochure panels using section classes such as `.p1` through `.p6`, with shared utility blocks like `.panel`, `.sheet`, and `.label`. There is no separate `src/`, `tests/`, or asset directory; QR codes and illustrations are embedded inline as SVG or base64 images.

## Build, Test, and Development Commands
There is no build step or package manager in this project.

- `python3 -m http.server 8000`
  Runs a local static server from the repository root for browser testing.
- `xdg-open http://localhost:8000`
  Opens the brochure in a browser on Linux after starting the server.
- `git diff --check`
  Catches trailing whitespace and malformed patches before commit.

For print validation, open the page in a browser and use print preview. The layout is designed around A4 landscape sheets (`297mm x 210mm`) with three `99mm` panels per side.

## Coding Style & Naming Conventions
Use 2-space indentation in HTML and CSS to match the existing file. Keep new styles inline inside the existing `<style>` block unless the repository structure changes. Prefer descriptive, panel-scoped class names such as `.p6-head` or `.pain-card`; avoid one-letter or overly generic selectors. Preserve Russian copy tone and keep visual content print-safe.

## Testing Guidelines
Testing is manual. After each content or layout change, verify:

- both brochure sides render without overflow or clipping
- print preview keeps panel widths and page breaks intact
- embedded QR images still render and remain scannable
- contact details and CTA text match the current marketing copy

## Commit & Pull Request Guidelines
Git history currently uses short imperative subjects, for example `Add buklet v11`. Follow that pattern: `Update CTA copy`, `Refine panel spacing`, `Add v12 brochure tweaks`. Keep commits focused on one visual or content change. Pull requests should include a brief summary, before/after screenshots or exported PDF pages, and note any print-specific checks performed.
