from django.contrib import admin
from .models import regexCombs, incidentLog

# Register your models here.
@admin.register(regexCombs)
class regexControlAdmin(admin.ModelAdmin):
    pass


@admin.register(incidentLog)
class incidentLogAdmin(admin.ModelAdmin):
    pass
