""" Class with the instance of a telepot bot and method to send messages"""
from dataclasses import dataclass
import os
from dotenv import load_dotenv
import telepot


dotenv_path = os.path.expanduser("./core/environ.env")
load_dotenv(dotenv_path=dotenv_path)


@dataclass
class Bot:
    """Telepot Bot instance"""

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    bot = telepot.Bot(BOT_TOKEN)

    def send_message(self, message, image) -> None:
        """
        This method takes a message and a randomize image to send telegram message

            Parameters:
                message (str): Message to be sent
                image (str): Url image to show with the message

            Returns:
                None
        """
        title = image[0].get("alt")
        self.bot.sendPhoto(self.CHAT_ID, image[0].get("data-srcset").split(" ")[0])
        self.bot.sendMessage(self.CHAT_ID, f"{title}\n{message} test")
