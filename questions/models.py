from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    answer_keywords = models.CharField(max_length=500)

