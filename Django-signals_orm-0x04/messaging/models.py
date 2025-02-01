from django.db import models
from django.contrib.auth.models import User


class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """
        Returns unread messages for a specific user.
        Optimized using `.only()` to fetch only necessary fields.
        """
        return self.filter(receiver=user, is_read=False).only("id", "sender", "content", "timestamp")


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)

    objects = UnreadMessagesManager()

    def mark_as_read(self):
        self.is_read = True
        self.save()


    def __str__(self):
        return f"{self.content} from {self.sender} to {self.receiver} ({'Read' if self.is_read else 'Unread'})"


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

    def __str__(self):
        return f'{self.sender} -> {self.receiver}: {self.content} (edited by {self.edited_by})'