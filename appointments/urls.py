from rest_framework.routers import DefaultRouter

from .views import AppointmentsViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet, basename='appointment')
urlpatterns = router.urls