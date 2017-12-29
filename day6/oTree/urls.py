# urls.py
from django.conf.urls import url, include
from otree.default_urls import urlpatterns

urlpatterns.append(
    url(r'^transcription/', include('real_effort1.ajax', namespace="real_effort1"))
)
