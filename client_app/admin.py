from django.contrib import admin
from .models import Department, Student

class TenantModelAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

@admin.register(Department)
class DepartmentAdmin(TenantModelAdmin):
    list_display = ('name',)  # Customize as needed

@admin.register(Student)
class StudentAdmin(TenantModelAdmin):
    list_display = ('name', 'place', 'department')  # Customize as needed
