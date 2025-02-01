from django.urls import path
from . import views

urlpatterns = [
    path('delete_user/', views.delete_user, name='delete_user'),
    path('' , views.home, name='home'),
    path('thread/', views.thread, name='thread'),
]