from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list=Question.objects.all()
    return render(request,"polls/index.html",{
        "latest_question_list":latest_question_list})

def detail(request, question_idd):
    question=get_object_or_404(Question,pk=question_idd)
    return render(request,"polls/detail.html",{
        "question":question
    })

def results(request, question_idd):
    return HttpResponse(f"Estas viendo resultados de la pregunta numero {question_idd}")


def vote(request, question_idd):
    return HttpResponse(f"Estas votando a la pregunta numero {question_idd}")

