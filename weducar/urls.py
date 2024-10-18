"""
URL configuration for weducar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, include
from django.contrib import admin
from drf_yasg import openapi

# swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="Weducar API",
        default_version='v0.1.0',
        description="API for Weducar - School Management System",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # Swagger e Redoc
    path(
        '', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
    path(
        'api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0),  name='schema-redoc',
    ),
    # Apps
    path(
        'api/v1/academics/', include('weducar.apps.academics.urls'), name="academics",
    ),
    path('api/v1/accounts/', include('weducar.apps.accounts.urls'), name="accounts",),
    path(
        'api/v1/administration/', include('weducar.apps.administration.urls'), name="administration",
    ),
    path(
        'api/v1/attendance/', include('weducar.apps.attendance.urls'), name="attendance",
    ),
    path(
        'api/v1/locations/', include('weducar.apps.locations.urls'), name="locations",
    ),
    path(
        'api/v1/management/', include('weducar.apps.management.urls'), name="management",
    ),
    path('api/v1/students/', include('weducar.apps.students.urls'), name="students",),
]
