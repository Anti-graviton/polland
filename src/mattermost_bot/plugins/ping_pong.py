import re

from mmpy_bot.bot import respond_to
from mmpy_bot.dispatcher import Message


@respond_to('ping', re.IGNORECASE)
def ping_pong(message: Message):
    message.reply('PONG!')
