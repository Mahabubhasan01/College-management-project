from django.contrib import admin
from .models import studentForm
# Register your models here.
""" @admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
        list_display = ['name'] """
admin.site.register(studentForm)