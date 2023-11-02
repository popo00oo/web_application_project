from django.contrib import admin

from lost.models import User, Lost, Notice

# Register your models here.

admin.site.register(User)
admin.site.register(Lost)
admin.site.register(Notice)