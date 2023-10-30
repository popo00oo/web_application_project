from django.contrib import admin
from app01.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserInfoAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "tel", "addr", "sex", "age", "role", "student_id")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "name", "tel", "age", "role", "is_staff", "student_id")

    list_filter = ("is_staff", "is_superuser", "role", "is_active", "groups", "age")

    search_fields = ("username", "name", "tel")


class HousingResource(resources.ModelResource):
    class Meta:
        model = House
        exclude = ['nid']


class HousingAdmin(ImportExportModelAdmin):
    list_display = ['building_no', 'housing_no', 'construction_area', 'using_area', 'type', 'create_date',
                    'user_name']

    list_filter = ['building_no', 'housing_no', 'type', 'user_name']

    list_per_page = 20

    resource_classes = [HousingResource]


class CrimeRateResource(resources.ModelResource):
    class Meta:
        model = CrimeRate
        import_id_fields = ['FID']
        exclude = ['nid']


class CrimeRateAdmin(ImportExportModelAdmin):
    list_display = ['X', 'Y', 'FID', 'Year', 'ReportDate', 'ReportTime', 'OccurDate', 'Occur_Time', 'Weekday',
                    'OffSummary', 'PrimViolat', 'Neighbourh', 'Sector', 'Division', 'CensusTra']

    resource_classes = [CrimeRateResource]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(House, HousingAdmin)
admin.site.register(CrimeRate, CrimeRateAdmin)

admin.site.site_header = 'Background management system'

admin.site.site_title = 'Background management system'
