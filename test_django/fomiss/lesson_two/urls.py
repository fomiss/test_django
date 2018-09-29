from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^items/$', views.items, name = "items"),
    re_path(r'^item/([0-9]{4,5})/$', views.year_archive, name = 'year_archive'),
    re_path(r'^item/([0-9]{4,5})/([0-9]{2})/$', views.month_archive, name = 'month_archive'),
    re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})/$', views.day_archive, name = 'day_archive'),
    re_path(r'^$', views.home),
    re_path(r'book/$', views.page, name ='page'),
    re_path(r'book/page(?P<num>[0-9]+)/$', views.page, name ='page'),
]