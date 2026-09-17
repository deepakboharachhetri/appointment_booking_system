from rest_framework.viewsets import ModelViewSet
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put','delete']  # noqa: RUF012

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    