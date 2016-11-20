from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','roll_num','aggregate')
    ordering= ('roll_num',)
    search_fields = ('roll_num','name',)

admin.site.register(Student,StudentAdmin)