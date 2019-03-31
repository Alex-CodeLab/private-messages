from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.utils import timezone
import uuid

def _uuid():
    return str(uuid.uuid4()).replace('-','')

class Conversation(models.Model):
    startdate   = models.DateTimeField(auto_now_add=True)
    users       = models.ManyToManyField(User)
    hash        = models.CharField(max_length=32,default=_uuid,unique=True)


class PrivateMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text    = models.TextField('text')
    persona = models.ForeignKey(User, related_name='persona', on_delete=models.CASCADE)
    personb = models.ForeignKey(User, related_name='personb', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[0:40]
