from rest_framework.routers import DefaultRouter

from .views import CityViewSet, StateViewSet, HousingViewSet, InstanceViewSet


app_name = 'locations'

router = DefaultRouter(trailing_slash=True)
router.register(r'states', StateViewSet, basename='state')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'housings', HousingViewSet, basename='housing')
router.register(r'instances', InstanceViewSet, basename='instance')

urlpatterns = router.urls
