from django.contrib import admin

from .models import (
    School, Employee, EmployeeSchool, ContractType,
    Position, Room, ScheduleGrid, ClassSchedule, Schooling
)

admin.site.register(School)
admin.site.register(Employee)
admin.site.register(EmployeeSchool)
admin.site.register(ContractType)
admin.site.register(Position)
admin.site.register(Room)
admin.site.register(ScheduleGrid)
admin.site.register(ClassSchedule)
admin.site.register(Schooling)
