from django import forms

from models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'answer_keywords',)
    
    question_text = forms.CharField()
    answer_keywords = forms.CharField(widget=forms.Textarea)

class AnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea)
