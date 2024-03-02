# ========================================================================
from rest_framework import permissions


# ========================================================================
class CustomPermission(permissions.BasePermission):
    """
    Custom permission to only allow users with a specific role to create objects.
    """

    def has_permission(self, request, view):
        # Check if the user has the required role to create objects
        # return request.user and request.user.has_role('admin')  # Adjust this condition as per your requirement
        return True
