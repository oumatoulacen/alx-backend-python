from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True # Uncomment this 2 lines if you want to allow anyone to read conversations
        return request.user and request.user.is_authenticated and request.user in obj.participants.all()

class IsSenderOfMessage(BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True # Uncomment this 2 lines if you want to allow anyone to read messages
        return request.user and request.user.is_authenticated and request.user == obj.sender
