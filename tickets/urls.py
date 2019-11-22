from django.conf.urls import url
from tickets.views import bug, addBug, bugDetails


urlpatterns = [
    url(r'^bug/', bug, name="bug"),
    url(r'^addBug/', addBug, name="addBug"),
    url(r'^bugDetails/(?P<pk>\d+)/$', bugDetails, name="bugDetails"),
]