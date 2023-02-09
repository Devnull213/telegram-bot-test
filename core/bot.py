from dataclasses import dataclass
from dotenv import load_dotenv
import telepot
import os


dotenv_path = os.path.expanduser("./core/environ.env")
load_dotenv(dotenv_path=dotenv_path)

@dataclass
class Bot:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    bot = telepot.Bot(BOT_TOKEN)

    def send_message(self, message, image) -> None:
        title = image[0].get("alt")
        self.bot.sendPhoto(self.CHAT_ID, image[0].get("data-srcset").split(" ")[0])
        self.bot.sendMessage(self.CHAT_ID, f"{title}\n{message} test")

