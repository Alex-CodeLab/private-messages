from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import Conversation

def conversations(request):
    conversations  = Conversation.objects.filter()
    contacts  = Conversation.objects.filter(users=request.user).values_list('users__username').distinct()
    return render(request, 'private_messages.html',{'contacts': contacts, 'conversations': conversations})


def conversation(request):
    #list
    try:
        conversation = Conversation.objects.get(hash= conversation_id)
    except ObjectDoesNotExist:
        pass
    return render(request, 'private_messages.html',{})
