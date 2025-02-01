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
    user = request.user
    messages = (
        Message.objects.filter(
        Q(sender=user) | Q(receiver=user),  # Either sender or receiver is the user
        parent_message__isnull=True)  # Only messages received by the user
        .select_related("sender", "parent_message")  # Optimize ForeignKey lookups
        .prefetch_related("replies")  # Prefetch all replies for each message
        .order_by("-timestamp")  # Show most recent messages first
    )
    print(messages)
    
    return render(request, "conversations.html", {"messages": messages})
