from rest_framework.viewsets import ModelViewSet
from .models import Service
from .serializers import ServiceSerializer
from accounts.permissions import IsStaff

class ServiceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put','delete']  # noqa: RUF012
    permission_classes = [IsStaff]  # noqa: RUF012
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    