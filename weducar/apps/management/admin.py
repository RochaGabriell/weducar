from django.contrib import admin

from .models import Classe, Shift, Week

admin.site.register(Classe)
admin.site.register(Shift)
admin.site.register(Week)
