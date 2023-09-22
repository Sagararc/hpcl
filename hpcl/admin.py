from django.contrib import admin
from .models import  CityModel , FormFieldModel,OutletModel ,OutletAssignmentModel,AttendanceModel
from accounts.models import Account
# Register your models here.


admin.site.register(CityModel)
admin.site.register(OutletModel)
admin.site.register(FormFieldModel)
admin.site.register(OutletAssignmentModel)
admin.site.register(AttendanceModel)
admin.site.register(Account)