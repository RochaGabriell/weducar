from rest_framework.routers import DefaultRouter

from .views import (
    HistoryAreaViewSet, HistoryViewSet, StudentClassesViewSet,
    StudentStatusViewSet, StudentViewSet, ColorViewSet
)


app_name = 'Students'

router = DefaultRouter(trailing_slash=True)
router.register(r'students', StudentViewSet, basename='students')
router.register(
    r'(?P<student_id>\d+)/classes', StudentClassesViewSet, basename='student_classes',
)
router.register(
    r'(?P<student_id>\d+)/status', StudentStatusViewSet, basename='student_status',
)
router.register(
    r'(?P<student_id>\d+)/history', HistoryViewSet, basename='student_history',
)
router.register(
    r'(?P<student_id>\d+)/history/(?P<history_id>\d+)/areas', HistoryAreaViewSet, basename='student_history_areas',
)
router.register(r'color', ColorViewSet, basename='student_color')


urlpatterns = router.urls
