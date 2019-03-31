from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import Conversation

def conversations(request):
    conversations  = Conversation.objects.filter()
    print(conversations)
    return render(request, 'private_messages.html',{'conversations': conversations})


def conversation(request):
    #list
    try:
        conversation = Conversation.objects.get(hash= conversation_id)
    except ObjectDoesNotExist:
        pass
    return render(request, 'private_messages.html',{})
