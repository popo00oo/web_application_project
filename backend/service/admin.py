from django.contrib import admin
from service.models import Lost, Notice


@admin.register(Lost)
class LostAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'date', 'category', 'upass', 'desc', 'status', 'create_time', 'update_time']
    list_editable = ['location', 'date', 'category', 'upass', 'desc', 'status']
    search_fields = ['category']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'create_time', 'update_time']
    list_editable = ['user', 'content']
    search_fields = ['user']
