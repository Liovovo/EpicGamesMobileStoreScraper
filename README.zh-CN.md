# Epic Games 移动端喜加一链接获取

本项目是一个简易 Python 脚本，用于从 Epic Games 移动端商店获取游戏信息，并生成可直接在浏览器中访问的游戏购买链接，适用于无法下载或不想下载手机APP的用户。

## 功能
- 无需登陆即可从 Epic Games 移动端商店获取游戏列表，包括喜加一游戏。
- 允许用户手动指定语言和地区。
- 生成可直接在浏览器中访问的游戏购买链接（需先在浏览器登录 epicgames 才能访问购买链接）。

## 当前免费游戏
以下内容可能已经过时。 **编辑时间: 2025/02/20**
- 《Dungeon of the Endless: Apogee》（锁国区）  
https://store.epicgames.com/purchase?&offers=1-6a99fb0a8add42c8b21c4ad25c928ba5-0fc96633957149ff8744aa1890145e2e
- 《Bloons TD 6》  
https://store.epicgames.com/purchase?&offers=1-6a8dfa6e441e4f2f9048a98776c6077d-c930e6f4d4e3420aad0241f45b0fea4b

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
