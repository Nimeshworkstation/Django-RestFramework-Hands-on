from django.contrib import admin
from .models import Student


@admin.register(Student)
class SingerAdmin(admin.ModelAdmin):
	list_display=['id','name','gender','city']

