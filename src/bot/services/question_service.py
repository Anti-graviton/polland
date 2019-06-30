"""
import QuerySet type from django db models
"""
from django.db.models.query import QuerySet

from web.models import Question


class QuestionService():
    """
    the question manager service, responsible for managing question-related actions
    """

    @staticmethod
    def list() -> QuerySet:
        """
        return a list of questions in descending creation_date order
        """
        result = Question.objects\
            .order_by('-creation_date')\
            .all()\
            .prefetch_related('choices')
        return result

    @staticmethod
    def get_question_with_id(qid) -> Question:
        """
        returns the question with id = qid
        """
        question = Question.objects\
            .prefetch_related('choices')\
            .get(pk=qid)

        return question
