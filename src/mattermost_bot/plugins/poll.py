import re

from mmpy_bot.bot import respond_to
from mmpy_bot.dispatcher import Message

from web.models import Question


@respond_to('list', re.IGNORECASE)
def get_question_list(msg: Message):
    all_questions = Question.objects.all()
    if Question.objects.count() == 0:
        msg.reply_thread(
            'Sorry, there are currently no questions in the database.')
    else:
        msg.reply(all_questions)
