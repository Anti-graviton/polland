DEBUG = False

# Docs + regexp or docs string only
PLUGINS_ONLY_DOC_STRING = False

BOT_LOGIN = 'polland@fanap.plus'
# BOT_PASSWORD = None
BOT_TEAM = 'FanapPlus'

# login with SSL verification
SSL_VERIFY = True

'''
# Custom default reply module

Example:
filename:
    my_default_reply.py
code:
    def default_reply(dispatcher, raw_msg):
        dispatcher._client.channel_msg(
            raw_msg['channel_id'], dispatcher.get_message(raw_msg)
        )
settings:
    DEFAULT_REPLY_MODULE = 'my_default_reply'
'''
DEFAULT_REPLY_MODULE = None

# or simple string for default answer
DEFAULT_REPLY = '''
### نمی‌فهمم چی می‌گی!
من یه ربات دون‌پایه‌ام! لطفا عین همین شیوه‌ای که این پایین نوشته با من صحبت کن.

|command|معنی|
|------|-----------------|
|list ‌ |‌دریافت لیست همه‌ی نظر‌سنجی‌های فعال|

'''

'''
If you use Mattermost Web API to send messages (with send_webapi()
or reply_webapi()), you can customize the bot logo by providing Icon or Emoji.
If you use Mattermost API to send messages (with send() or reply()),
the used icon comes from bot settings and Icon or Emoji has no effect.
'''
BOT_ICON = 'http://lorempixel.com/64/64/abstract/7/'
BOT_EMOJI = ':godmode:'
