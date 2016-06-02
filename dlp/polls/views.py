from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    Returns all the choices in a table with their coresponding vote count.
    """
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        # 'choices': choices,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    choice_id = request.POST['choice']
    question = get_object_or_404(Question, pk=question_id)
    choice = Choice.objects.filter(pk=choice_id)[0]
    choice.votes += 1 
    choice.save()
    response = HttpResponseRedirect(reverse('results', args=(question.id,)))
    return response
