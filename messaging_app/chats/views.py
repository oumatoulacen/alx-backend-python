from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer


# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        participant_ids = request.data.get('participants')

        filters = {
            'participants': participant_ids,
        }

        if not filters['participants']:
            return Response({"error": "participants is required."}, status=400)

        if not participant_ids or len(participant_ids) < 2:
            return Response({"error": "At least two participants are required."}, status=400)

        participants = User.objects.filter(user_id__in=participant_ids)
        if len(participants) != len(participant_ids):
            return Response({"error": "Some participants do not exist."}, status=404)

        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=201)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=False, methods=['post'])
    def send_message(self, request):
        conversation_id = request.data.get('conversation_id')
        sender_id = request.data.get('sender_id')
        message_body = request.data.get('message_body')

        filters = {
            'conversation_id': conversation_id,
            'sender_id': sender_id,
            'message_body': message_body,
        }
        if not all(filters.values()):
            return Response({"error": "conversation_id, sender_id, and message_body are required."}, status=400)
    
        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation does not exist."}, status=404)

        try:
            sender = User.objects.get(user_id=sender_id)
        except User.DoesNotExist:
            return Response({"error": "Sender does not exist."}, status=404)

        if sender not in conversation.participants.all():
            return Response({"error": "Sender is not part of the conversation."}, status=403)

        message = Message.objects.create(sender=sender, conversation=conversation, message_body=message_body)
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=201)
