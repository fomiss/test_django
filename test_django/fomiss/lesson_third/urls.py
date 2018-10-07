from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^view/$', views.view),
    re_path(r'^filters/$', views.filter),
    re_path(r'^tags-if/$', views.tags_if),
    re_path(r'^tags-for/$', views.tags_for),
    re_path(r'^base/$', views.base),
    re_path(r'^adrian/$', views.adrian),
    ]
