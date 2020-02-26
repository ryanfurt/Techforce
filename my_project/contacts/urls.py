from django.conf.urls import url
from django.contrib import admin

from .views import(
    contact_list,
    contact_create,
    contact_detail,
    contact_update,
    contact_delete,
)

urlpatterns = [
    url(r'^$', contact_list, name="list"),
    url(r'^create/$', contact_create),
    url(r'^(?P<id>\d+)/$', contact_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', contact_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', contact_delete),
]
