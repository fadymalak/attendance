from rest_framework.permissions import BasePermission




class UserOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # for retrieve method
        user = request.user
        obj_user = obj.employee.user
        return user == obj_user
