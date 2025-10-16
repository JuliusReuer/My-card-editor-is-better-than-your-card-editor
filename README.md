# My Card Editor Is Better Than Your Card Editor (MCBTYC) — Save / Deck Editor

A save file editor and toolkit for the game "My Card Is Better Than Your Card" (MCBTYC).  
This repository provides utilities to load, inspect, and modify game save files, card data, and decks, plus a simple GUI to create and manage runs.

## Features
- Parse and inspect game save files and CSV data resources.
- Read / modify card objects, stickers/effects, and event data.
- Simple UI for opening saves, editing decks and running save edits.
- Utilities for importing/exporting decks (CSV/plaintext).

## Requirements
- Python 3.10+ recommended
- Common dependencies: (tkinter for GUI, pandas optional for CSV work)
  - tkinter usually included with standard Python installers on Windows.
  - If you use pandas: pip install pandas

## Installation / Setup
1. Clone the repository:
   ```cmd
   git clone https://github.com/JuliusReuer/My-card-editor-is-better-than-your-card-editor
   ```

## Quickstart — Run the editor
- From the project root (Windows PowerShell or cmd):
  - Launch the simple GUI editor:
    python main.py

If you use VS Code, use the provided .vscode/launch.json to run or debug main.py.

## Project layout (summary)
- main.py — application entry point / scripts
- data_loader.py — CSV and save parsing utilities
- const.py — global constants
- classes/ — core logic and domain models
  - DataClassUnpack.py — data unpacking and helpers
  - save_data/ — save-file domain models (event, other, cards, event_data)
- ui/ — simple GUI and editors
  - main_editor.py — UI launcher
  - Editor/save_manager.py — save management in UI
- data/ — CSV resources and example decks

See top of repository for the full file list.

## Data files & formats
- CSV resources live in data/ (character_data.csv, sticker_data.csv, toy_data.csv, and decks/).
- Custom Decks will be stored in the JSON format in data/decks/.
- Save parsing assumes the game's save binary/format — be careful and backup saves before editing.

## Usage examples
- CLI is not currently planed
- Just run the main.py file

## Development notes
- Make packages importable by adding __init__.py files in classes/ and ui/ if you plan to import submodules.
- Prefer package-style imports (e.g. from classes.save_data.cards.card import Card) after adding __init__.py.
- Keep data/ as read-only resources; modify saves only with backups.

Recommended small changes:
- Create classes/__init__.py and classes/save_data/__init__.py to re-export commonly used classes.
- Add a tests/ directory and basic unit tests for parsing functions.
- Add a requirements.txt if you pin third-party packages.

## Contributing
- Fork → feature branch → PR
- Keep changes small and focused.
- Add tests for parsing or save-format changes.
- Document any breaking changes to save format handling in this README.

## Troubleshooting
- GUI doesn't start: ensure tkinter is available (standard Windows Python includes it).
- Import errors after reorganizing packages: add __init__.py and update imports to package-style.
- Always back up original save files before editing.

## License
This repository includes a LICENSE file. Review it before distributing edited save files or derived work.

## Contact
For project issues, open an issue in this repository with a reproducible description and steps.
