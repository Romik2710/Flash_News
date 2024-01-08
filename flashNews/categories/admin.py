from django.contrib import admin
from .models import UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(UserData, UserDataAdmin)
