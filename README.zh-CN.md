# Epic Games 移动端喜加一链接获取

本项目是一个简易 Python 脚本，用于从 Epic Games 移动端商店获取游戏信息，并生成可直接在浏览器中访问的游戏购买链接，适用于无法下载或不想下载手机APP的用户。

## 功能
- 无需登陆即可从 Epic Games 移动端商店获取游戏列表，包括喜加一游戏。
- 允许用户手动指定语言和地区。
- 生成可直接在浏览器中访问的游戏购买链接（需先在浏览器登录 epicgames 才能访问购买链接）。
- （目前默认为安卓，如需ios请手动修改代码URL中的platform=android为platform=ios，部分地区无ios游戏列表）

## 当前免费游戏
以下内容可能已经过时。 **编辑时间: 2025/02/21**
- 《STAR WARS™ Knights of the Old Republic™》(Android)  
[https://store.epicgames.com/purchase?&offers=1-6a99fb0a8add42c8b21c4ad25c928ba5-0fc96633957149ff8744aa1890145e2e](https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-9e4d37c87517463ab3363f35feb59a21)
- 《STAR WARS™ Knights of the Old Republic™ II - The Sith Lords™》(Android)  
[https://store.epicgames.com/purchase?&offers=1-6a8dfa6e441e4f2f9048a98776c6077d-c930e6f4d4e3420aad0241f45b0fea4b](https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-594bef97f68348cd9de9a296a0ae69d3)
- 《STAR WARS™ Knights of the Old Republic™》(ios)  
[https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-d8d2c735ab0545269b0b8547e52de9d6](https://store.epicgames.com/purchase?&offers=1-f678054a89a64b53b4edb5fe0664f410-d8d2c735ab0545269b0b8547e52de9d6)
- 《STAR WARS™ Knights of the Old Republic™ II - The Sith Lords™》(ios)  
[https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-9e52f37e06d04ec1bde77d1d321fd07a](https://store.epicgames.com/purchase?&offers=1-6be6051edd0740e984b9c891791d6691-9e52f37e06d04ec1bde77d1d321fd07a)

## 使用方法

运行脚本：
```sh
python epic_mobile.py
```

或直接从 Releases 下载打包好的 `epic_mobile.exe` 并运行。

## 依赖项
- Python 3.x
- requests
- cloudscraper
- tabulate

## Screenshot
![screenshot01](https://github.com/user-attachments/assets/16992e39-aba2-46be-ad58-7585610a7723)

## 许可协议
GPL-3.0 许可证
