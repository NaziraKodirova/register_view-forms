from django.contrib import admin
from .models import Address, Student
from import_export.admin import ImportExportModelAdmin


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'status_display', 'student_address')

    def status_display(self, obj):
        return obj.get_status_display()

    def student_address(self, obj):
        return obj.address
