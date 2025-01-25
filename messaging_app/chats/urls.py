from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet

# Root router
router = routers.DefaultRouter()
router.register('conversations', ConversationViewSet, basename='conversation')

# Nested router for messages under conversations
nested_router = routers.NestedDefaultRouter(router, 'conversations', lookup='conversation')
nested_router.register('messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
