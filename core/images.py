import random
import requests
from bs4 import BeautifulSoup

class Images:
    def __init__(self):
        self.url = "https://www.thrillophilia.com/places-to-visit-in-germany"
        self.data = requests.get(self.url)

    def parse_data(self) -> list:
        try:
            xml_parsed_data = BeautifulSoup(self.data.content, "lxml")
            images = xml_parsed_data.find_all("div", {"class": "base-block main-card-container content-main-card"})
            return images
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)

    def randomize_images(self):
        images = self.parse_data()
        random_img = random.randint(0, len(images) - 1)
        image = images[random_img].find_all("img")
        return image

