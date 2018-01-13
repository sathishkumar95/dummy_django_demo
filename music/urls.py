from django.urls import include, path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]
