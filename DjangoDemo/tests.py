import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionMethodTests(TestCase):
    def was_published_recently(self):
        # should return False for questions whose pub_date is in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)
