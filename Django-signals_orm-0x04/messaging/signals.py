from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(receiver=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def create_message_history(sender, instance, **kwargs):
    print("\n\n*******************\ninstance\n\n", instance, "\n\n*******************\ninstance\n\n")
    if instance: # Check if the message is being updated
        MessageHistory.objects.create(sender=instance.sender, receiver=instance.receiver, content=instance.content)