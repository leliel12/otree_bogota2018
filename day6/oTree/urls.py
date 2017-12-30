# urls.py
from django.conf.urls import url, include
from otree.default_urls import urlpatterns

urlpatterns.extend([
    url(r'^transcription0/', include('real_effort0.ajax', namespace="real_effort0")),
    url(r'^transcription1/', include('real_effort1.ajax', namespace="real_effort1")),
    url(r'^transcription2/', include('real_effort2.ajax', namespace="real_effort2"))
])
