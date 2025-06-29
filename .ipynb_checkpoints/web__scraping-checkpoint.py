import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def scrape_page(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=(10, 20))

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            products = soup.find_all("div", class_="a-card__inc")

            product_data = []

            for product in products:
                image_tag = product.find("a", class_="a-card__image")
                image_link = image_tag.find("img")["src"] if image_tag and image_tag.find("img") else "N/A"

                title_tag = product.find("a", class_="a-card__title")
                title = title_tag.text.strip() if title_tag else "N/A"

                price_tag = product.find("div", class_="a-card__price")
                price = price_tag.text.strip().replace('\xa0', ' ') if price_tag else "N/A"

                subtitle_tag = product.find("div", class_="a-card__subtitle")
                subtitle = subtitle_tag.text.strip() if subtitle_tag else "N/A"

                text_preview_tag = product.find("div", class_="a-card__text-preview")
                text_preview = text_preview_tag.text.strip() if text_preview_tag else "N/A"

                view_count_tag = product.find("span", class_="a-view-count status-item")
                view_count = view_count_tag.text.strip() if view_count_tag else "N/A"

                product_data.append({
                    "Image Link": image_link,
                    "Title": title,
                    "Price": price,
                    "Subtitle": subtitle,
                    "Text Preview": text_preview,
                    "View Count": view_count
                })
            print(f"Successfully retrieved the page: {url}")
            return product_data
        else:
            print(f"Failed to retrieve page: {url}")
            return []
    except requests.exceptions.ConnectTimeout:
        print(f"Connection to {url} timed out.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while requesting {url}: {e}")
        return []


base_url = "https://krisha.kz/arenda/kvartiry/almaty/?das[_sys.hasphoto]=1&rent-period-switch=%2Farenda%2Fkvartiry&page="

all_product_data = []

for page in range(1, 8): 
    url = f"{base_url}{page}"  
    page_data = scrape_page(url)
    all_product_data.extend(page_data)

    time.sleep(5)  

print(all_product_data)

df = pd.DataFrame(all_product_data)

df.to_csv("renting_flats_Almaty.csv", index=False)