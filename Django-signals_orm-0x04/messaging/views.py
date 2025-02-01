from django.shortcuts import render, redirect
from django.http import HttpResponse

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