import logging
import sys

from mmpy_bot.bot import Bot

logging.basicConfig(**{
    'format': '[%(asctime)s] %(message)s',
    'datefmt': '%m/%d/%Y %H:%M:%S',
    'level': logging.DEBUG,
    'stream': sys.stdout,
})

if __name__ == "__main__":
    polland_bot: Bot = Bot()
    polland_bot.run()
