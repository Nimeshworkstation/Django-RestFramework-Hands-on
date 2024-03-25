from django.contrib import admin
from .models import Singer, Song


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
	list_display=['id','name','gender']

# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ['id','title','singer','duration']
