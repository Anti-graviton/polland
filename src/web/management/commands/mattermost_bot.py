import logging
import sys

from django.conf import settings
from django.core.management.base import BaseCommand
from mmpy_bot.bot import Bot


class Command(BaseCommand):
    def handle(self, **options):

        logging.basicConfig(**{
            'format': '[%(asctime)s] %(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
            'level': logging.DEBUG,
            'stream': sys.stdout,
        })

        try:
            polland_bot: Bot = Bot()
            polland_bot._plugins.plugins.append('mattermost_bot.plugins')
            polland_bot.run()
        except KeyboardInterrupt:
            pass
