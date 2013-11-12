from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from forms import QuestionForm
from models import Question

def index(request):
    questions = Question.objects.all()
    return render(request, "questions/index.html", { "questions": questions })

def add(request):
    if request.method != 'POST':
       question_form = QuestionForm()
       return render(request, "questions/add.html", { "form": question_form })

    question_form = QuestionForm(request.POST)
    if not question_form.is_valid():
       return render(request, "questions/add.html", { "form": question_form })
    
    question_text = question_form.cleaned_data['question_text']
    answer_keywords = question_form.cleaned_data['answer_keywords']
    Question.objects.create(question_text=question_text, answer_keywords=answer_keywords)
    
    return HttpResponseRedirect(reverse("questions_index"))
