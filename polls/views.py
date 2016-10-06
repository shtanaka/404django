from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
Class IndexView(request):

		
Class DetailsView(request, question_id):


Class ResultsView(request, question_id):


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'details.html', { 'question': question, 'error_message': "You did not select a choice!"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

