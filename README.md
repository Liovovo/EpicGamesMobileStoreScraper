# EpicGamesLinkExtraction

Epic Games 喜加一游戏的直达领取链接思路，链接可供用户直接通过网页端领取仅能通过移动端获取的免费游戏。


## 链接结构分析
Epic游戏购买链接格式：
https://store.epicgames.com/purchase?&offers=1-[sandboxId]-[offerId]

- `clientName=egs-android`：移动端标识，通常在请求时需要添加以访问移动端页面。
- `offers`：抓包移动端APP获取的游戏相关的标识：
  - `sandboxId`
  - `offerId`

完整的 `offers` 参数格式为：`1-[sandboxId]-[offerId]`。

## 示例链接
以下为两个示例游戏的直达领取链接：
- 《Dungeon of the Endless: Apogee》
https://store.epicgames.com/purchase?&offers=1-6a99fb0a8add42c8b21c4ad25c928ba5-0fc96633957149ff8744aa1890145e2e&showNavigation=true
- 《Bloons TD 6》
https://store.epicgames.com/purchase?&offers=1-6a8dfa6e441e4f2f9048a98776c6077d-c930e6f4d4e3420aad0241f45b0fea4b
