from django.urls import path
from .AudioFileInterface import create_audio_file
from .views import read_audio_file  , delete_audio_file, update_audio_file

urlpatterns = [

    path("create/", create_audio_file),
    path("file/<str:file_type>/", read_audio_file ),
    path("file/<str:file_type>/<int:file_id>", read_audio_file ),
    path("remove/<str:file_type>/<int:file_id>", delete_audio_file ),
    path("update/<str:file_type>/<int:file_id>", update_audio_file )
]