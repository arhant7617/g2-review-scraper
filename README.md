# G2 Review Scraper

A simple Python-based web scraper that extracts customer reviews from G2 for a given product and saves them in structured JSON format.

---

## 🚀 Features

- Scrapes reviews from G2 product pages
- Supports pagination (multiple pages of reviews)
- Filters reviews by date range
- Extracts:
  - Review title
  - Review text
  - Rating
  - Review date
- Outputs clean JSON data
- Beginner-friendly and easy to extend

---

## 🛠️ Tech Stack

- Python 3
- requests
- BeautifulSoup (bs4)
- python-dateutil

---

## Project Structure

g2-review-scraper/
    │
    ├── g2_scraper.py
    ├── reviews.json
    └── README.md
## How to Run
python g2_scraper.py

[
{
    "title": "Great collaboration tool",
    "review": "Slack has improved our team communication...",
    "rating": "5",
    "date": "2024-03-12"
}
]

