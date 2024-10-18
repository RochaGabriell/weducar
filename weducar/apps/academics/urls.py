from rest_framework.routers import DefaultRouter

from .views import (
    SchoolYearViewSet, AcademicYearViewSet, EvaluationViewSet,
    CurricularComponentViewSet, LessonContentViewSet, DiaryViewSet,
    GradeViewSet, CurricularComponentMatrixViewSet, CurricularMatrixViewSet
)


app_name = 'Academics'

router = DefaultRouter(trailing_slash=True)
router.register(r'school-years', SchoolYearViewSet, basename='school-year')
router.register(
    r'academic-years', AcademicYearViewSet, basename='academic-year'
)
router.register(r'evaluations', EvaluationViewSet, basename='evaluation')
router.register(
    r'curricular-components', CurricularComponentViewSet, basename='curricular-component'
)
router.register(
    r'lessons-content', LessonContentViewSet, basename='lesson-content'
)
router.register(r'diaries', DiaryViewSet, basename='diary')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(
    r'curricular-components-matrix', CurricularComponentMatrixViewSet,
    basename='curricular-component-matrix'
)
router.register(
    r'curricular-matrix', CurricularMatrixViewSet, basename='curricular-matrix'
)


urlpatterns = router.urls
