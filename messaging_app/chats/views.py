from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        participants = User.objects.filter(user_id__in=[participant for participant in participants])
        if len(participants) < 2:
            return Response({'participants': 'Conversations must have at least 2 participants.'}, status=status.HTTP_400_BAD_REQUEST)
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        conversation_id = kwargs.get('conversation_pk')
        conversation = Conversation.objects.get(conversation_id=conversation_id)
        sender = User.objects.get(user_id=request.data['user_id'])
        message_body = request.data['message_body']
        message = Message.objects.create(conversation=conversation, sender=sender, message_body=message_body)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
