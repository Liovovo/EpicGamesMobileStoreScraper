English | [简体中文](./README.zh-CN.md)

# Epic Games Mobile Store Scraper

This project is a Python script that scrapes game information from the Epic Games mobile store and generates game purchase links that can be accessed directly in a browser. This is useful for iOS users outside the EU and those who do not want to download the mobile app.(If you need the purchase link for iOS, please manually change the URL in the code from Android to iOS.)

## Features
- Retrieve a list of games from the Epic Games mobile store, including limited-time free games.
- Allow users to manually specify country code and language.
- Generate game purchase links that can be accessed directly in a browser.

## Free Games
The following content may be outdated. **Last updated: February 21, 2025**
- 《STAR WARS™ Knights of the Old Republic™》(Android)  
[https://store.epicgames.com/purchase?&offers=1-6a99fb0a8add42c8b21c4ad25c928ba5-0fc96633957149ff8744aa1890145e2e](https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-9e4d37c87517463ab3363f35feb59a21)
- 《STAR WARS™ Knights of the Old Republic™ II - The Sith Lords™》(Android)  
[https://store.epicgames.com/purchase?&offers=1-6a8dfa6e441e4f2f9048a98776c6077d-c930e6f4d4e3420aad0241f45b0fea4b](https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-594bef97f68348cd9de9a296a0ae69d3)
- 《STAR WARS™ Knights of the Old Republic™》(ios)  
[https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-d8d2c735ab0545269b0b8547e52de9d6](https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-d8d2c735ab0545269b0b8547e52de9d6)
- 《STAR WARS™ Knights of the Old Republic™ II - The Sith Lords™》(ios)  
[https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-9e52f37e06d04ec1bde77d1d321fd07a](https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-9e52f37e06d04ec1bde77d1d321fd07a)

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
