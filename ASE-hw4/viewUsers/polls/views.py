from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice
from django.utils import timezone

def index(request):
	q = Question(question_text="What's new?", pub_date=timezone.now())
	q.save()
	q.id
	q.question_text
	q.pub_date
	return HttpResponse("<h1>"+q.question_text+"<h1>")