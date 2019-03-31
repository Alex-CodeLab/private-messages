from django.contrib import admin

from .models import Conversation, PrivateMessage

admin.site.register(Conversation)
admin.site.register(PrivateMessage)
