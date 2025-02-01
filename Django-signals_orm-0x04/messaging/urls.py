from django.urls import path
from . import views

urlpatterns = [
    path('delete_user/', views.delete_user, name='delete_user'),
    path('conversations/', views.user_conversations_view, name='conversations'),
]