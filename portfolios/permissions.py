from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite edición solo al dueño del objeto.
    """

    def has_object_permission(self, request, view, obj):
        # Lectura: permitido para todos los usuarios autenticados
        if request.method in permissions.SAFE_METHODS:
            return True
        # Escritura: solo el dueño
        return obj.user == request.user
