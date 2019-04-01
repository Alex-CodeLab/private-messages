from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Conversation

def conversations(request):
    conversations  = Conversation.objects.filter(users=request.user)
    userids = conversations.values_list('users__id').distinct()
    contacts = User.objects.filter(id__in=userids)
    return render(request, 'private_messages.html',{'contacts': contacts, 'conversations': conversations})


def conversation(request):
    #list
    try:
        conversation = Conversation.objects.get(hash= conversation_id)
    except ObjectDoesNotExist:
        pass
    return render(request, 'private_messages.html',{})
