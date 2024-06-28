from django.contrib import admin
from .models import Account, Material, License, Employee, NewEmployee, AllKeys, Role, Other, Installation

# Register your models here.
admin.site.register(Account)
admin.site.register(Material)
admin.site.register(Employee)
admin.site.register(NewEmployee)
admin.site.register(AllKeys)
admin.site.register(Other)
admin.site.register(Installation)

class LicenseAdmin(admin.ModelAdmin):
    fields = ['licensename']
    list_display = ['licenseID', 'licensename']
    list_filter = ['licensename']

admin.site.register(License, LicenseAdmin)

# Check if Role model is already registered before registering it again
if not admin.site.is_registered(Role):
    admin.site.register(Role)
