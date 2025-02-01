from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message, Notification, MessageHistory

# Create your views here.
def delete_user(request):
    '''Delete a user and all related data'''
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'delete_user.html')

def home(request):
    '''Home page'''
    return HttpResponse('Home page')

def thread(request):
    '''Thread page'''
    # Get all replies to the parent message and related_messages
    message = Message.objects.prefetch_related('replies').first() # prefetch_related is used to reduce the number of queries
    return render(request, 'thread.html', {'message': message})
