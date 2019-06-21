import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from bot import mattermost_bot


class Command(BaseCommand):
    def handle(self, **options):

        try:
            bot = mattermost_bot.PollandBot()
            bot.start()
        except KeyboardInterrupt:
            logging.error('stopping but due to keyboard interrupt')
            pass
