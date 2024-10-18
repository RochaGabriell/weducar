from django.contrib import admin

from .models import City, State, Housing, Instance

admin.site.register(City)
admin.site.register(State)
admin.site.register(Housing)
admin.site.register(Instance)
