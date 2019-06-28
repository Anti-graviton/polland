"""
module imports
"""
import os
import re

from django.db.models.query import QuerySet
from mmpy_bot.bot import respond_to
from mmpy_bot.dispatcher import Message

from web.models import Choice, Question

from ..services.question_service import QuestionService

QUESTION_SERVICE = QuestionService()


@respond_to('list', re.IGNORECASE)
def get_question_list(msg: Message):
    """
    hadnle the list command
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


@respond_to('q:(.*) a:(.*)', re.IGNORECASE)
def answer_question(msg: Message, question_id: str, answer_id: str):
    """
    Mark a question as answerd with specific answer for a user
    """
    # TODO: log user information
    # TODO: update user answer
    question: Question = QUESTION_SERVICE.get_question_with_id(question_id)
    q_answer: Choice = question.choices.get(id=int(answer_id))
    msg.reply_thread("You just answered question: {} with option: {}".format(
        question, q_answer.value))


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
