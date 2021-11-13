from .views import Contest
from django.urls import path

urlpatterns = [
    path('file_generator', Contest.generate_file, name="file_generator"),
    path('download_file', Contest.download_file, name="download_file"),
]
