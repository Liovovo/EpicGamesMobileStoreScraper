import json
import requests
import time
import random
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import cloudscraper
from tabulate import tabulate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

country = input("Enter country code (e.g., US): ").strip()
locale = input("Enter locale (e.g., en-US): ").strip()

API_URL = f"https://egs-platform-service.store.epicgames.com/api/v2/public/discover/home?count=10&country={country}&locale={locale}&platform=android&start=0&store=EGS"

HEADERS = {
    "User-Agent": "Ktor client",
    "Accept": "application/json",
    "Accept-Language": locale,
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

def fetch_json():
    logger.info("Initializing CloudScraper...")
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )
    try:
        logger.info("Accessing Epic Games Store homepage...")
        scraper.get("https://store.epicgames.com/", headers=HEADERS)
        time.sleep(random.uniform(1, 3))  # Simulate real user behavior
        logger.info("Sending API request to fetch game data...")
        response = scraper.get(API_URL, headers=HEADERS)

        if response.status_code == 200:
            logger.info("Successfully fetched data")
            return response.json()
        else:
            logger.error(f"Failed to fetch data, status code: {response.status_code}")
            return {}
    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        return {}

def parse_games(data):
    logger.info("Parsing game data...")
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
                "offer_id": offer_id
            })
    logger.info(f"Parsing complete, retrieved {len(games)} games")
    return games

def display_games(games):
    logger.info("Displaying game list...")
    headers = ["ID", "Game Name", "Category", "Original Price", "Discount", "Current Price", "Purchase Type"]
    table = [[game["ID"], game["Game Name"], game["Category"], game["Original Price"], game["Discount"], game["Current Price"], game["Purchase Type"]] for game in games]
    print(tabulate(table, headers=headers, tablefmt="simple_outline"))

def get_purchase_link(game):
    return f"https://store.epicgames.com/purchase?&offers=1-{game['sandbox_id']}-{game['offer_id']}"

if __name__ == "__main__":
    logger.info("Starting Epic Games Mobile Store Scraper...")
    logger.info("https://github.com/Liovovo/EpicGamesMobileStoreScraper")
    data = fetch_json()
    games = parse_games(data)
    display_games(games)

    while True:
        user_input = input("Enter game ID (or 'q' to quit): ")
        if user_input.lower() == 'q':
            logger.info("User exited program")
            break
        if user_input.isdigit() and int(user_input) < len(games):
            game = games[int(user_input)]
            logger.info(f"Fetching purchase link for {game['Game Name']}...")
            print(f"Purchase Link: {get_purchase_link(game)}\n")
        else:
            logger.warning("Invalid input, please try again.")