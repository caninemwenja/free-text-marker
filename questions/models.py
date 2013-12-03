import re

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_keywords = models.CharField(max_length=500)
    
    def regex(self):
        keywords = [x.strip() for x in self.answer_keywords.split(",")]
        regex = "|".join(keywords)
        return regex
    
    def match(self, answer):
        matcher = re.compile(self.regex(), re.IGNORECASE)
        return matcher.search(answer)
    
