from django.contrib import admin
from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'is_active', 'create_time', 'update_time']
    list_editable = ['username', 'password', 'is_active']
