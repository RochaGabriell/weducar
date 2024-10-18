from django.contrib import admin

from .models import (
    JustifiedAbsence, Frequency, SysPresence
)

admin.site.register(JustifiedAbsence)
admin.site.register(Frequency)
admin.site.register(SysPresence)
