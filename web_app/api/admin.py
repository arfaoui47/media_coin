from django.contrib import admin

from .models import Time, Extension


class TimeAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'total_spent', 'created', 'updated')

admin.site.register(Time, TimeAdmin)


class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('user', "extension", 'created', 'updated')

admin.site.register(Extension, ExtensionAdmin)