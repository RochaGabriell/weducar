from rest_framework.routers import DefaultRouter

from .views import FrequencyViewSet, JustifiedAbsenceViewSet, SysPresenceViewSet


app_name = 'Attendance'

router = DefaultRouter(trailing_slash=True)
router.register(r'frequencies', FrequencyViewSet, basename='frequencies')
router.register(
    r'justified-absences', JustifiedAbsenceViewSet, basename='justified-absences'
)
router.register(r'sys-presences', SysPresenceViewSet, basename='sys-presences')

urlpatterns = router.urls
