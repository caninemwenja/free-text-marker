from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from forms import QuestionForm

def index(request):
    return render(request, "questions/index.html")

def add(request):
    if request.method != 'POST':
       question_form = QuestionForm()
       return render(request, "questions/add.html", { "form": question_form })
    
    return HttpResponseRedirect(reverse("questions_index"))
