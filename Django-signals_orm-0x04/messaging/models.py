from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)

    def mark_as_read(self):
        self.is_read = True
        self.save()

class Notification(models.Model):
    receiver = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

class MessageHistory(models.Model):
    sender = models.ForeignKey(User, related_name='sent_history', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_history', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, related_name='edited_history', on_delete=models.CASCADE)