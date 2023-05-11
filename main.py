import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://omsk.mlsn.ru/arenda-nedvizhimost/?onlyOwners=1"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

blocks = soup.find_all("div", class_="realty-item")

flats = []

for block in blocks:

    nameFlat = block.find("a", class_="location").get_text().strip()

    flat = {
        "Кварира": nameFlat,
    }

    flats.append(flat)

df = pd.DataFrame(flats)
df.to_excel('flats.xlsx', index=False)