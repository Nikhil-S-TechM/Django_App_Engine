from django.urls import path
from home.views import *

urlpatterns = [
    path('', index, name='index'),
    path('ffmpeg/', run_ffmpeg, name='ffmpeg'),
    path('start_process/', start_process, name="start_process"),
    path('show_process/', show_process, name="show_process"),

]
