from django.contrib import admin

from employee_list.models import *

@admin.register(Department)
class DepAdmin(admin.ModelAdmin):
    list_display = ["dep_name"]

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ["tit_name"]

@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):
    list_display = ["second_name", "name", "last_name"]