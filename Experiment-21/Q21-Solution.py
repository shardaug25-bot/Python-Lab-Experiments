# Experiment 21: Product Scraping and CSV

import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter e-commerce webpage URL: ")

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    # Find product containers
    items = soup.select(
        ".product, .product-card, .product_pod"
    )

    for item in items:
        name_tag = item.select_one(
            ".title, .product-title, h2, h3"
        )
        price_tag = item.select_one(
            ".price, .product-price, .price_color"
        )
        link_tag = item.find("a", href=True)

        if name_tag:
            name = name_tag.get_text(strip=True)
            price = (
                price_tag.get_text(strip=True)
                if price_tag else "Not available"
            )
            link = (
                urljoin(url, link_tag["href"])
                if link_tag else "Not available"
            )

            products.append([name, price, link])

    # Save information to CSV
    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Product Name", "Price", "Product Link"])
        writer.writerows(products)

    print("\nProducts extracted:", len(products))
    print("Data saved in products.csv")

    if not products:
        print("No products found. The website may use different HTML classes.")

except requests.exceptions.RequestException as e:
    print("Website access error:", e)