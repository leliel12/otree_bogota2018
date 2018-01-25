from django.conf.urls import url, include
from otree.default_urls import urlpatterns


urlpatterns.extend([
    url(r'^transcription/', include('reffort.ajax', namespace="reffort"))])
