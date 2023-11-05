from django.contrib import admin
from lost.models import User, Lost, Notice
from django.contrib.auth.hashers import make_password


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Your code for the admin display list, search fields, etc.

    def save_model(self, request, obj, form, change):
        # Only hash the password if it's a new object or if the password has been changed
        if not change or 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)


# The other models can just be registered normally if you don't need custom admin logic

admin.site.register(Lost)
admin.site.register(Notice)

'''
admin.site.register(User)
admin.site.register(Lost)
admin.site.register(Notice)
'''
