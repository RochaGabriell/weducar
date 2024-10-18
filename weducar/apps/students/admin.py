from django.contrib import admin

from .models import Student, History, HistoryArea, StudentStatus, StudentClasses

admin.site.register(Student)
admin.site.register(History)
admin.site.register(HistoryArea)
admin.site.register(StudentStatus)
admin.site.register(StudentClasses)
