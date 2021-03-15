from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SongFile)
class SongFileAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "uploaded_time"]
    search_fields = ["name"]

@admin.register(PodcastFile)
class PodcastFileAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "uploaded_time", "host", "participants"]
    search_fields = ["name"]

@admin.register(AudiobookFile)
class AudiobookFileAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "uploaded_time", "narrator", "author"]
    search_fields = ["name"]
