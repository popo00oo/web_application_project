from django.contrib import admin
from lost.models import User, Lost, Notice
from django.contrib.auth.hashers import make_password


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):


    def save_model(self, request, obj, form, change):
        # Hash the password will use when create a new object
        if not change or 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)



admin.site.register(Lost)
admin.site.register(Notice)

'''
admin.site.register(User)
admin.site.register(Lost)
admin.site.register(Notice)
'''
