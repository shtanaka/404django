from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
from django.http import HttpResponse
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'index.html', context)
		
def details(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'details.html', {'question': question})

def results(request, question_id):
	return HttpResponse("You're looking for results of question %s" % (question_id))

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % (question_id))

