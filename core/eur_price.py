from bs4 import BeautifulSoup
from dataclasses import dataclass
import requests
import math

@dataclass
class GetEurData:
    url: str = "https://www.eleconomista.es/cruce/EURCLP"
    data = requests.get(url, timeout=5)

    def get_price(self):
        xml_parsed_data = BeautifulSoup(self.data.content, "lxml")
        conversion_value = xml_parsed_data.find(
            "span", {"class": "last-value"}
        )
        return conversion_value


    def convert_price(self) -> tuple:
        price = self.get_price()
        formatting = price.text[:-3].replace(',', '.')
        final_price = f'{math.ceil(float(formatting) * 1210):,}'
        return formatting, final_price


