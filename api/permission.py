from operator import truediv
from rest_framework import permissions

class IsStaffPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        value = request.user.is_staff
        if value: 
            return True
        else: 
            return False