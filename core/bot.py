from dotenv import load_dotenv
from pathlib import Path
import telepot
import os

dotenv_path = Path("./environ.env")
load_dotenv(dotenv_path=dotenv_path)

class Bot:
    def __init__(self):
        self.BOT_TOKEN = os.environ["BOT_TOKEN"]
        self.CHAT_ID = os.environ["CHAT_ID"]
        self.bot = telepot.Bot(self.BOT_TOKEN)

    def send_message(self, message, image) -> None:
        title = image[0].get("alt")
        self.bot.sendPhoto(self.CHAT_ID, image[0].get("data-srcset").split(" ")[0])
        self.bot.sendMessage(self.CHAT_ID, f"{title}\n{message} test")

