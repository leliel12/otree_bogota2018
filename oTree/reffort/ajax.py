
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r"^validate_transcription/$" ,
        views.validate_transcription, name="validate_transcription")]
