from django import forms

from models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'answer_keywords',)
    
    text = forms.CharField()
    answer_keywords = forms.CharField(widget=forms.Textarea)

