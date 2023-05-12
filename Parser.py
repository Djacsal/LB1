import requests
import pandas as pd
from bs4 import BeautifulSoup

flats = []
def scrape_flats():
    url = "https://omsk.mlsn.ru/arenda-nedvizhimost/?onlyOwners=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    blocks = soup.find_all("div", class_="realty-item")

    for block in blocks:
        nameFlat = block.find("a", class_="location").get_text().strip()
        flat = {
            "Список квартир": nameFlat,
        }
        flats.append(flat)

def save_to_excel(filename):
    df = pd.DataFrame(flats)
    df.to_excel(filename, index=False)