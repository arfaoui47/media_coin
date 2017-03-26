from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')

admin.site.register(Profile, ProfileAdmin)