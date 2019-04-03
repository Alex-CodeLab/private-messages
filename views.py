from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Conversation, PrivateMessage

def conversations(request, conversation_hash = None):
    # if hash provided, show messages
    if conversation_hash:
        try:
            conversation = Conversation.objects.get(hash= conversation_hash)
            private_messages = PrivateMessage.objects.filter(conversation= conversation).order_by('id')
        except ObjectDoesNotExist:
            return redirect('/private/')
    else:
        private_messages = []

    conversations  = Conversation.objects.filter(users=request.user)
    userids  = conversations.values_list('users__id').distinct()
    contacts = User.objects.filter(id__in=userids)

    return render(request, 'private_messages.html',{'contacts': contacts, 'private_messages': private_messages})

def conversation(request):
    #list
    try:
        conversation = Conversation.objects.get(hash= conversation_id)
    except ObjectDoesNotExist:
        pass
    return render(request, 'private_messages.html',{})
