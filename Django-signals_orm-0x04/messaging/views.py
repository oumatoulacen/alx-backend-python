from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Message
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def delete_user(request):
    '''Delete a user and all related data'''
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'delete_user.html')


@login_required
def user_conversations_view(request):
    """
    Fetch all conversations involving the logged-in user.
    """
    messages = (
        Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user),  # Either sender or receiver is the user
        parent_message__isnull=True)  # Only messages received by the user
        .select_related("sender", "parent_message")  # Optimize ForeignKey lookups
        .prefetch_related("replies")  # Prefetch all replies for each message
        .order_by("-timestamp")  # Show most recent messages first
    )    
    return render(request, "conversations.html", {"messages": messages})


@login_required
def unread_messages_view(request):
    """
    Displays unread messages for the logged-in user.
    """
    unread_messages = Message.objects.unread_for_user(request.user)
    
    return render(request, "unread_messages.html", {"messages": unread_messages})