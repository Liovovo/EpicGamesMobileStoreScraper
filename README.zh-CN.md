# Epic Games 移动端喜加一链接获取

本项目是一个简易 Python 脚本，用于从 Epic Games 移动端商店获取游戏信息，并生成可直接在浏览器中访问的游戏购买链接，适用于无法下载或不想下载手机APP的用户。

## 功能
- 无需登陆即可从 Epic Games 移动端商店获取游戏列表，包括喜加一游戏。
- 允许用户手动指定语言、地区和系统。
- 生成可直接在浏览器中访问的游戏购买链接（需先在浏览器登录 epicgames 才能访问购买链接）。
- 全自动获取当前限免游戏购买链接，支持单个及一键入库（类似于购物车购买多个物品）。

## 使用方法

运行脚本：
```sh
python epic_mobile.py
```
如果只想获取限免游戏购买链接：
```sh
python epic_mobile_FREE_US_zh-CN.py
```

或直接从 Releases 下载打包好的 `epic_mobile_XXX.exe` 并运行。


## 依赖项
- Python 3.x
- requests
- cloudscraper
- tabulate

## Screenshot
![screenshot01](https://github.com/user-attachments/assets/16992e39-aba2-46be-ad58-7585610a7723)

## 许可协议
GPL-3.0 许可证
