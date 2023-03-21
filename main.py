from core.images import Images
from core.bot import Bot
from core.utils import message
import cProfile
import pstats

def main() -> None:
    """Main execution function"""
    msg, msg2 = message()
    random_image = image.randomize_images()
    bot.send_message(msg, msg2, random_image)


if __name__ == "__main__":
    image = Images()
    bot = Bot()
    main()

