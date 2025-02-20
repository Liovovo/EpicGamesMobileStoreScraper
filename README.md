English | [简体中文](./README.zh-CN.md)

# Epic Games Mobile Store Scraper

This project is a Python script that scrapes game information from the Epic Games mobile store and generates game purchase links that can be accessed directly in a browser. This is useful for iOS users outside the EU and those who do not want to download the mobile app.

## Features
- Retrieve a list of games from the Epic Games mobile store, including limited-time free games.
- Allow users to manually specify country code and language.
- Generate game purchase links that can be accessed directly in a browser.

## Free Games
The following content may be outdated. **Last updated: February 21, 2025**
- 《STAR WARS™ Knights of the Old Republic™》  
[https://store.epicgames.com/purchase?&offers=1-6a99fb0a8add42c8b21c4ad25c928ba5-0fc96633957149ff8744aa1890145e2e](https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-9e4d37c87517463ab3363f35feb59a21)
- 《STAR WARS™ Knights of the Old Republic™ II - The Sith Lords™》  
[https://store.epicgames.com/purchase?&offers=1-6a8dfa6e441e4f2f9048a98776c6077d-c930e6f4d4e3420aad0241f45b0fea4b](https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-594bef97f68348cd9de9a296a0ae69d3)

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
