"""
module imports
"""
import os
import re
import datetime

from django.db.models.query import QuerySet
from mmpy_bot.bot import respond_to
from mmpy_bot.dispatcher import Message

from web.models import Choice, Question, UserAnswer

from ..services.question_service import QuestionService

QUESTION_SERVICE = QuestionService()


@respond_to('list', re.IGNORECASE)
def get_question_list(msg: Message):
    """
    handle the list command
    """
    msg.reply_thread('بذار ببینم چه سوالایی رو می‌تونی جواب بدی... :thinking:')

    all_questions: QuerySet = QUESTION_SERVICE.list()

    if all_questions.count() == 0:
        msg.reply_thread(
            'ببخشید ولی مثکه دستمون خالیه، سوالی برای جواب دادن نیست :disappointed_relieved:')
    else:

        for question in all_questions:
            question_str = get_question_representation(question)
            msg.reply(question_str)


@respond_to('(.*)-(.*)', re.IGNORECASE)
def answer_question(msg: Message, question_id: str, answer_id: str):
    """
    Mark a question as answerd with specific answer for a user
    """
    try:
        question: Question = QUESTION_SERVICE.get_question_with_id(question_id)
        q_answer: Choice = question.choices.get(id=int(answer_id))
        user_id = user_name = msg.body['data']['sender_name']
        obj, created = UserAnswer.objects\
            .update_or_create(user_id=user_id,
                              question_id=question.id,
                              defaults={
                                  'answer_date': datetime.datetime.now(),
                                  'answer_id': q_answer.id,
                                  'question_id': question.id,
                                  'user_name': user_name,
                                  'user_id': user_id
                              })

        obj.save()

        if created:
            msg.reply('نظر شما به سوال فوق ثبت شد!')
        else:
            msg.reply('نظر شما به سوال فوق عوض شد!')
    except Exception:
        msg.reply_thread('خطا! داده‌های ورودی رو بررسی کن و دوباره تلاش کن.')


def get_question_representation(question: Question):
    """
    generate question and it's choices string representation
    """
    question_str = "{}. {}{}".format(question.id, question.title, os.linesep)
    for choice in question.choices.all():
        question_str += create_question_answers(question, choice)
    question_str += os.linesep

    question_str += "***"
    return question_str


def create_question_answers(question: Question, choice: Choice) -> str:
    """
    generate a choice string representation
    """
    result = "{}-{}. {}{}"\
        .format(question.id,
                choice.id,
                choice.value,
                os.linesep)
    return result
