import logging
import sys
from datetime import datetime

from mmpy_bot.bot import Bot, settings, MessageDispatcher


class PollandBot(Bot):

    def __init__(self):
        logging.basicConfig(**{
            'format': '[%(asctime)s] %(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
            'level': logging.DEBUG,
            'stream': sys.stdout,
        })

        settings.DEFAULT_REPLY = '''
# نمی‌فهمم چی می‌گی!
من یه ربات دون‌پایه‌ام! لطفا عین همین شیوه‌ای که این پایین نوشته با من صحبت کن.


|command|معنی|
|------|-----------------|
|list ‌ |‌دریافت لیست همه‌ی نظر‌سنجی‌های فعال|
|‪`q:`*شماره سوال* ‌`a:`*شماره جواب*  |‫‌پاسخ به یه نظرسنجی|
|   مثال:   | ‪q:**1**<فاصله>a:**3** => گزینه‌ی ۳ برای سوال شماره ۱ |

'''

        self.bot: Bot = Bot()
        self.bot._plugins.plugins.append('bot.plugins')

    def start(self):
        self.bot.run()
        print('Polland bot started at: {}'.format(datetime.now()))
