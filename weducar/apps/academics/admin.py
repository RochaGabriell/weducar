from django.contrib import admin

from .models import (
    SchoolYear, AcademicYear, Evaluation, CurricularComponent,
    LessonContent, Diary, Grade, CurricularComponentMatrix, CurricularMatrix
)

admin.site.register(SchoolYear)
admin.site.register(AcademicYear)
admin.site.register(Evaluation)
admin.site.register(CurricularComponent)
admin.site.register(LessonContent)
admin.site.register(Diary)
admin.site.register(Grade)
admin.site.register(CurricularComponentMatrix)
admin.site.register(CurricularMatrix)
