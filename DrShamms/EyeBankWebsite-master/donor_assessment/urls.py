from django.urls import path
from .views import home, upload_file, get_prompt, submit_question
from django.conf import settings
from django.conf.urls.static import static
from .views import get_latest_json

urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_file, name="upload_file"),
    path("get_prompt/", get_prompt, name="get_prompt"),
    path('submit_question/', submit_question, name='submit_question'),
    path('get-latest-json/', get_latest_json, name='get_latest_json'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)