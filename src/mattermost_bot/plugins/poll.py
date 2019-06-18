import re
import os

from mmpy_bot.bot import respond_to
from mmpy_bot.dispatcher import Message

from web.models import Question, Choice, ChoiceType


@respond_to('list', re.IGNORECASE)
def get_question_list(msg: Message):
    all_questions = Question.objects.order_by(
        '-publish_date').all().prefetch_related('choices')

    if Question.objects.count() == 0:
        msg.reply_thread(
            'Sorry, there are currently no questions in the database.')
    else:
        for idx, q in enumerate(all_questions):
            question_str = "{}. {}".format(idx+1, q.title)
            question_str += os.linesep
            choices = [c for c in q.choices.values()]
            for cidx, c in enumerate(choices):
                question_str += "{}/{}. {}{}".format(
                    idx+1, cidx+1, c['value'], os.linesep)
            question_str += os.linesep
            question_str += "---"

            msg.reply(question_str)
