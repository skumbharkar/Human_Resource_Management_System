
from django.contrib import admin

# Register your models here.

from .models import admin_info,employee_info,employee_leaves_details,leave_count,department

admin.site.register(admin_info)
admin.site.register(employee_info)
admin.site.register(employee_leaves_details)
admin.site.register(leave_count)
admin.site.register(department)