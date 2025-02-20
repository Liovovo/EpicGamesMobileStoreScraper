English | [简体中文](./README.zh-CN.md)

# Epic Games Mobile Store Scraper

This project is a Python script that scrapes game information from the Epic Games mobile store and generates game purchase links that can be accessed directly in a browser.

## Features
- Retrieve a list of games from the Epic Games mobile store, including limited-time free games.
- Allow users to manually specify country code and language.
- Generate game purchase links that can be accessed directly in a browser.

## Free Games
The following content may be outdated. **Last updated: February 20, 2025**
- 《Dungeon of the Endless: Apogee》
https://store.epicgames.com/purchase?&offers=1-6a99fb0a8add42c8b21c4ad25c928ba5-0fc96633957149ff8744aa1890145e2e
- 《Bloons TD 6》
https://store.epicgames.com/purchase?&offers=1-6a8dfa6e441e4f2f9048a98776c6077d-c930e6f4d4e3420aad0241f45b0fea4b

## Usage

Run the script (dependencies required):
```sh
python epic_mobile.py
```
Or download `epic_mobile.exe` from Releases and run.

## Dependencies
- Python 3.x
- requests
- cloudscraper
- tabulate
  
## Screenshot
![screenshot01](https://github.com/user-attachments/assets/16992e39-aba2-46be-ad58-7585610a7723)

## License
GPL-3.0 license
