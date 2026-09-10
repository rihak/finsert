# Finsert

[![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)]()
[![Single file](https://img.shields.io/badge/build-single%20file-blue)]()
[![Made with vanilla JS](https://img.shields.io/badge/JS-vanilla-yellow)]()

🚀 **[Try FInsert live](https://rihak.github.io/finsert/)** — no install needed, just open the link.

**Finsert** is a zero-dependency, single-file browser tool that turns a raw SQL `INSERT INTO` statement into a clear, editable column ↔ value table — so you can immediately see which value belongs to which field, without counting commas by hand.

It also supports a **side-by-side compare mode**, useful for spotting differences between two INSERT statements (for example, two rows from an audit trail).

## Features

- 🔍 **Instant parsing** — paste a SQL `INSERT INTO` statement and get a readable table of column/value pairs.
- ✏️ **Bidirectional editing** — edit a value directly in the table, or edit the raw SQL text; both stay in sync.
- 🧠 **Resilient parser** — correctly handles nested function calls (`to_date(...)`), quoted strings with commas, escaped quotes (`''`), and multi-line queries; malformed input degrades gracefully instead of silently dropping data.
- 🆚 **Compare mode** — load a second query side by side and highlight the differences, at the word or character level.
- 🖱️ **No install, no build step** — it's a single HTML file with everything (markup, styles, and logic) inlined. Just open it in a browser.
- 🎓 **Guided tour** — a built-in walkthrough introduces every feature interactively.
- 💾 **Session persistence** — your last queries and settings are remembered via `localStorage`.

## Usage

Try it instantly at **[https://rihak.github.io/finsert/](https://rihak.github.io/finsert/)**, or open [`index.html`](index.html) locally in any modern browser — no build tools, package manager, or server required.

On first load, the guided tour walks you through the main features; you can restart it anytime from the **Tour** button.

## Why

Reading a long `INSERT INTO table (col1, col2, ...) VALUES (val1, val2, ...)` statement and matching each value to its column by eye is tedious and error-prone, especially with many columns or long text values. Finsert removes that friction — paste the query, get an aligned table back.

## Roadmap

- [ ] PWA support (installable, offline-first)

## Contributing

Issues and pull requests are welcome. Since this is a single-file project with no build step, changes can be tested by simply opening `index.html` in a browser.

## Author

Made by [Riccardo Pietrini](https://github.com/rihak).
