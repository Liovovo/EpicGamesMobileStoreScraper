import json
import requests
import time
import random
import logging
import cloudscraper
from tabulate import tabulate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

COUNTRY = "US"
LOCALE = "en-US"
PLATFORMS = ["android", "ios"]

BASE_API_URL = "https://egs-platform-service.store.epicgames.com/api/v2/public/discover/home"
HEADERS = {
    "User-Agent": "Ktor client",
    "Accept": "application/json",
    "Accept-Language": LOCALE,
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

def fetch_json(platform):
    logger.info(f"Fetching game data for platform: {platform}")
    api_url = f"{BASE_API_URL}?count=10&country={COUNTRY}&locale={LOCALE}&platform={platform}&start=0&store=EGS"
    scraper = cloudscraper.create_scraper(browser={"browser": "chrome", "platform": "windows", "mobile": False})
    try:
        scraper.get("https://store.epicgames.com/", headers=HEADERS)
        time.sleep(random.uniform(1, 3))
        response = scraper.get(api_url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to fetch data for {platform}, status code: {response.status_code}")
            return {}
    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        return {}

def parse_games(data, platform):
    games = []
    for category in data.get("data", []):
        category_title = category.get("title", "Uncategorized")
        for offer in category.get("offers", []):
            content = offer.get("content", {})
            title = content.get("title", "Unknown Game")
            purchase_info = content.get("purchase", [{}])[0]
            sandbox_id = purchase_info.get("purchasePayload", {}).get("sandboxId", "")
            offer_id = purchase_info.get("purchasePayload", {}).get("offerId", "")
            price = purchase_info.get("priceDisplay", "Free")
            discount = purchase_info.get("discount", {}).get("discountAmountDisplay", "None")
            original_price = purchase_info.get("discount", {}).get("originalPriceDisplay", price)
            purchase_type = purchase_info.get("purchaseType", "Unknown")
            games.append({
                "ID": len(games),
                "Game Name": title,
                "Category": category_title,
                "Original Price": original_price,
                "Discount": discount,
                "Current Price": price,
                "Purchase Type": purchase_type,
                "sandbox_id": sandbox_id,
                "offer_id": offer_id,
                "Platform": platform
            })
    return games

def display_games(platform_games):
    for platform, games in platform_games.items():
        logger.info(f"Displaying game list for {platform.upper()}...")
        headers = ["ID", "Game Name", "Category", "Original Price", "Discount", "Current Price", "Purchase Type"]
        table = [[game["ID"], game["Game Name"], game["Category"], game["Original Price"], game["Discount"], game["Current Price"], game["Purchase Type"]] for game in games]
        print(f"\nPlatform: {platform.upper()}\n")
        print(tabulate(table, headers=headers, tablefmt="simple_outline"))

def get_purchase_link(game):
    return f"https://store.epicgames.com/purchase?&offers=1-{game['sandbox_id']}-{game['offer_id']}"

def get_free_games_links(platform_games):
    free_links = []
    all_free_games = []
    output_lines = []
    
    for platform, games in platform_games.items():
        for game in games:
            if game["Original Price"] != "Free" and game["Current Price"] == "Free":
                link = get_purchase_link(game)
                free_links.append(link)
                all_free_games.append(f"1-{game['sandbox_id']}-{game['offer_id']}")
                output_lines.append(f"{game['Game Name']} ({platform.upper()}):\n{link}\n")
    
    if all_free_games:
        combined_link = "https://store.epicgames.com/purchase?&offers=" + "&offers=".join(all_free_games)
        print(f"\nAll purchase links:\n{combined_link}\n")
    
    for line in output_lines:
        print(line)
    
    if not output_lines:
        print("\nNo free games available.\n")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    logger.info("Starting Epic Games Mobile Store Scraper...")
    platform_games = {platform: parse_games(fetch_json(platform), platform) for platform in PLATFORMS}
    display_games(platform_games)
    input("\nPress Enter to display free game purchase links...")
    get_free_games_links(platform_games)
