from django.conf.urls import url
from tickets.views import bug, addBug


urlpatterns = [
    url(r'^bug/', bug, name="bug"),
    url(r'^addBug/', addBug, name="addBug"),
]