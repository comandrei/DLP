from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })

def detail(request, question_id):
    print 'detail'
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    print 'results'
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request, 'polls/results.html', {})

def vote(request, question_id):
    print 'vote'
    question = get_object_or_404(Question, pk=question_id)
    response = HttpResponseRedirect(reverse('results', args=(question.id,)))
    return response
    # return render(request, 'polls/detail.html', {})
    #               # return HttpResponse("You're voting on question %s." % question_id)
