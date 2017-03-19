from django.contrib import admin

from .models import Time


class TimeAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'total_spent', 'created', 'updated')

admin.site.register(Time, TimeAdmin)