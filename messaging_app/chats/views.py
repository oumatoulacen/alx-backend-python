from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation, IsSenderOfMessage


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        # using filters
        filters = participants
        participants = User.objects.filter(user_id__in=[participant for participant in participants])

        if len(set(filters)) != len(set(participants)):
            return Response({'participants': 'Conversations cannot have duplicate participants.'}, status=status.HTTP_400_BAD_REQUEST)

        if len(set(participants)) < 2:
            return Response({'participants': 'Conversations must have at least 2 participants.'}, status=status.HTTP_400_BAD_REQUEST)
        
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsSenderOfMessage]

    def create(self, request, *args, **kwargs):
        conversation_id = kwargs.get('conversation_pk')
        conversation = Conversation.objects.get(conversation_id=conversation_id)
        sender = User.objects.get(user_id=request.data['user_id'])
        message_body = request.data['message_body']
        message = Message.objects.create(conversation=conversation, sender=sender, message_body=message_body)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
