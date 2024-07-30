from django.contrib import admin
from home.models import Contact, JobSeeker, City, Qualification, Employee

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'address', 'contactno', 'email', 'message', 'date')

class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'address', 'city', 'contactno', 'email', 'qualification', 'file', 'date')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empid', 'name', 'fname', 'mname', 'gender', 'address', 'city', 'contactno', 'email', 'department', 'designation', 'dob', 'doj', 'salary')

class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)

class QualificationAdmin(admin.ModelAdmin):
    list_display = ('qualification',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Employee, EmployeeAdmin)