from django.contrib import admin

from .models import Student, History, HistoryArea, StudentStatus, StudentClasses, Color

admin.site.register(Student)
admin.site.register(History)
admin.site.register(HistoryArea)
admin.site.register(StudentStatus)
admin.site.register(StudentClasses)
admin.site.register(Color)
