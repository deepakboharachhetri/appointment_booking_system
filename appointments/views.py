from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ServiceSerializer
from .models import Service
from accounts.permissions import IsStaff


class ServiceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put','delete']  # noqa: RUF012
    queryset = Service.objects.all()
    permission_classes = [IsStaff]
    serializer_class = ServiceSerializer