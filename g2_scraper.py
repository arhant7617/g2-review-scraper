import requests
import json
from bs4 import BeautifulSoup
from dateutil import parser
import time

BASE_URL = "https://www.g2.com/products/{}/reviews?page={}"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_g2_reviews(company_slug, start_date, end_date):
    page = 1
    reviews = []

    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)

    while True:
        print("Scraping page", page)
        url = BASE_URL.format(company_slug, page)
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        review_blocks = soup.select("div.paper")

        if not review_blocks:
            break

        for block in review_blocks:
            try:
                title = block.select_one("h3").text.strip()
                body = block.select_one("div[itemprop='reviewBody']").text.strip()
                rating = block.select_one("span[itemprop='ratingValue']").text.strip()
                date_text = block.select_one("time")["datetime"]
                review_date = parser.parse(date_text)

                if review_date < start_date or review_date > end_date:
                    continue

                reviews.append({
                    "title": title,
                    "review": body,
                    "rating": rating,
                    "date": review_date.strftime("%Y-%m-%d")
                })
            except:
                continue

        page += 1
        time.sleep(1)

    return reviews

company = input("Enter company name (example: slack): ")
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")

data = scrape_g2_reviews(company, start, end)

with open("reviews.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("DONE! Reviews saved in reviews.json")
