from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_keywords = models.CharField(max_length=500)

