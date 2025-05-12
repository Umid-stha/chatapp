from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

User = get_user_model()

def deserialize_user(user):
    return {
        'id': user.id, 'username':user.username, 'email':user.email,
        'first_name':user.first_name, 'last_name':user.last_name
    }

class TrackableDateModel(models.Model):

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

def generate_unique_uri():
    return str(uuid4()).replace("-", '')[:15]

class ChatSession(TrackableDateModel):

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    uri = models.URLField(default=generate_unique_uri)

class ChatSessionMessages(TrackableDateModel):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    chat_session = models.ForeignKey(ChatSession,related_name="messages", on_delete=models.PROTECT)
    message = models.TextField(max_length=2000)

    def to_json(self):
        return {'user': deserialize_user(self.user), 'message': self.message}
    
class ChatSessionMembers(TrackableDateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    chat_session = models.ForeignKey(ChatSession,related_name="members", on_delete=models.PROTECT)