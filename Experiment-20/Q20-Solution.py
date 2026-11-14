# Experiment 20: Extract News Headlines and Hyperlinks

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Take webpage URL from user
url = input("Enter news website URL: ")

try:
    # Send request
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )

    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    print("\nNews Headlines and Hyperlinks\n")

    count = 0

    # Find all heading tags
    for heading in soup.find_all(["h1", "h2", "h3", "h4"]):

        headline = heading.get_text(" ", strip=True)

        if not headline:
            continue

        # Find link inside heading
        link = heading.find("a", href=True)

        if link:
            hyperlink = urljoin(url, link["href"])
        else:
            # Check parent for a link
            parent_link = heading.find_parent("a", href=True)

            if parent_link:
                hyperlink = urljoin(url, parent_link["href"])
            else:
                hyperlink = "No hyperlink found"

        print("Headline:", headline)
        print("Link:", hyperlink)
        print("-" * 60)

        count += 1

    if count == 0:
        print("No headlines found.")

except requests.exceptions.RequestException as e:
    print("Error accessing website:", e)

