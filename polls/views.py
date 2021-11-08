from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from polls.models import Participant
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


import random
poll_group=['A','B','C','D','E']

def index(request):
    return render(request, 'polls/index.html')

def game(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    content = {
        'participant' : participant
    }
    return render(request, 'polls/game.html', content)

def participate(request):
    participant = Participant()
    participant.group=random.choice(poll_group)
    participant.save()
    return redirect('polls:game', participant.id)

@csrf_exempt
def submit(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if(request.method == 'POST'):
        participant.history = str(request.POST.get('hist', ''))
        participant.save()
    return redirect('polls:index')