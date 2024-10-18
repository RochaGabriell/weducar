from rest_framework.routers import DefaultRouter

from .views import ClasseViewSet, ShiftViewSet, WeekViewSet


app_name = 'management'

router = DefaultRouter(trailing_slash=True)
router.register(r'classes', ClasseViewSet, basename='classes')
router.register(r'shifts', ShiftViewSet, basename='shifts')
router.register(r'weeks', WeekViewSet, basename='weeks')

urlpatterns = router.urls
