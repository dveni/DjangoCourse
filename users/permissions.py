from rest_framework.permissions import BasePermission



class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Defines if authenticated user in request.user is permitted to do
        the action (GET, POST, PUT, DELETE)
        :param request:
        :param view:
        :return:
        """

        if view.action == 'create':
            return True
        elif request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'update', 'destroy']:
            return True
        else:
            #GET to /api/1.0/users/
            return False

    def has_object_permission(self, request, view, obj):
        """
        Defines if authenticated user in request.user is permitted to do
        the action (GET, PUT, DELETE) over the object obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        #If is superuser or the owner
        return request.user.is_superuser or request.user == obj