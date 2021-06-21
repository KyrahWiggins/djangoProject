from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from DjangoDemo import models
from DjangoDemo.models import Choice


def vote(request, primary_key):
    question = get_object_or_404(models.Question, id=primary_key)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "u didn't select a choice."
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=question.id))


def detail(request):
    return None


def results(request):
    return None


def index(request):
    return None
