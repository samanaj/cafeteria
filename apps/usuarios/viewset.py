from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets

from .models import User
from .serializer import UserSerializer

from .pagination import CustomPagination
# from .permissions import IsOwnerOrReadOnly, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = CustomPagination
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)