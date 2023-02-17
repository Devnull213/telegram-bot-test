"""Module to get and manage images"""
from dataclasses import dataclass
import random
from bs4 import BeautifulSoup
import requests


@dataclass
class Images:
    """ Class that gets webscrapped info and returns the urls"""
    url: str = "https://www.thrillophilia.com/places-to-visit-in-germany"
    data = requests.get(url, timeout=2)

    def parse_data(self) -> list:
        """
        Parser function to the website
            
            Parameters:
                None

            Returns:
                Parsed url images list
        """
        try:
            xml_parsed_data = BeautifulSoup(self.data.content, "lxml")
            images = xml_parsed_data.find_all(
                "div", {"class": "base-block main-card-container content-main-card"}
            )
            return images
        except requests.exceptions.RequestException as error:
            raise SystemExit(error) from error

    def randomize_images(self):
        """
        Returns a random image from a list

            Parameters:
                None
            
            Returns:
                Single randomized url image
        """
        images = self.parse_data()
        random_img = random.randint(0, len(images) - 1)
        image = images[random_img].find_all("img")
        return image
