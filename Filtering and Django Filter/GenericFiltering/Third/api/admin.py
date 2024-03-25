from django.contrib import admin
from .models import StudentAPI

# Register your models here.

@admin.register(StudentAPI)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id','name','roll','city','passby']