from django.db import models
import uuid

# Create your models here.
# Database Specification
# Entities and Attributes

# User:
# user_id (Primary Key, UUID, Indexed)
# first_name (VARCHAR, NOT NULL)
# last_name (VARCHAR, NOT NULL)
# email (VARCHAR, UNIQUE, NOT NULL)
# password_hash (VARCHAR, NOT NULL)
# phone_number (VARCHAR, NULL)
# role (ENUM: 'guest', 'host', 'admin', NOT NULL)
# created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

# Message:
# message_id (Primary Key, UUID, Indexed)
# sender_id (Foreign Key, references User(user_id))
# message_body (TEXT, NOT NULL)
# sent_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

# Conversation:
# conversation_id (Primary Key, UUID, Indexed)
# participants_id (Foreign Key, references User(user_id)
# created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

# Using the tables definition described above,

# Create the user Model an extension of the Abstract user for values not defined in the built-in Django User model
# Create the conversation model that tracks which users are involved in a conversation
# Create the message model containing the sender, conversation as defined in the shared schema attached to this project

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
