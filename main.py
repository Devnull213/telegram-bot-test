from core.images import Images
from core.bot import Bot
from core.utils import message

def main() -> None:
    """Main execution function"""
    msg = message()
    random_image = image.randomize_images()
    bot.send_message(msg, random_image)


if __name__ == "__main__":
    image = Images()
    bot = Bot()
    main()
