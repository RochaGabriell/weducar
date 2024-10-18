from rest_framework.routers import DefaultRouter

from .views import (
    ClassScheduleViewSet, ContractTypeViewSet, EmployeeSchoolViewSet,
    EmployeeViewSet, PositionViewSet, RoomViewSet,
    ScheduleGridViewSet, SchoolViewSet, SchoolingViewSet
)

app_name = 'administration'

router = DefaultRouter(trailing_slash=True)
router.register(
    r'class-schedule', ClassScheduleViewSet, basename='class-schedule',
)
router.register(
    r'contract-type', ContractTypeViewSet, basename='contract-type',
)
router.register(
    r'employee-school', EmployeeSchoolViewSet, basename='employee-school',
)
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'position', PositionViewSet, basename='position')
router.register(r'room', RoomViewSet, basename='room')
router.register(
    r'schedule-grid', ScheduleGridViewSet, basename='schedule-grid',
)
router.register(r'school', SchoolViewSet, basename='school')
router.register(r'schooling', SchoolingViewSet, basename='schooling')

urlpatterns = router.urls
