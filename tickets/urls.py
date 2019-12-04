from django.conf.urls import url
from tickets.views import bug, addBug, bugDetails, upvote, edit_bug


urlpatterns = [
    url(r'^bug/', bug, name="bug"),
    url(r'^addBug/', addBug, name="addBug"),
    url(r'^bugDetails/(?P<pk>\d+)/$', bugDetails, name="bugDetails"),
    url(r'^upvote/(?P<pk>\d+)/$', upvote, name="upvote"),
    url(r'^edit_bug/(?P<pk>\d+)/$', edit_bug, name="edit_bug"),
]