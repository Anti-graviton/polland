import re

from mmpy_bot.bot import respond_to


@respond_to('ping', re.IGNORECASE)
def ping_pong(message):
    message.reply('PONG!')
