from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from accounts.permissions import IsStaff

from .models import Appointment
from .serializers import AppointmentSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class AppointmentsViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch','delete']  # noqa: RUF012
    filter_backends = [DjangoFilterBackend]  # noqa: RUF012
    filterset_fields = ['status']  # noqa: RUF012
    queryset = Appointment.objects.all()
    permission_classes = [IsStaff]  # noqa: RUF012
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request, pk=None):
        appointment = self.get_object()
        new_status = request.data.get('status')

        if new_status not in dict(Appointment.STATUS_CHOICES):
            return Response({"error": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

        appointment.status = new_status
        appointment.save()

        return Response({"status": "Status updated successfully."}, status=status.HTTP_200_OK)

