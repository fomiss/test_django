from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/', include([
            re_path(r'^hystory/$', views.hystory),
            re_path(r'^edit/$', views.edit),
            re_path(r'^discuss/$', views.discuss),
            re_path(r'^permissions/$', views.permissions),
    ])),
]
# urlpatterns = [
#     re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/hystory/$', views.hystory),
#     re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/edit/$', views.edit),
#     re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/discuss/$', views.discuss),
#     re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/permissions/$', views.permissions),
# ]
#
# extra_patterns = [
#     re_path(r'report/$', views.report),
#     re_path(r'report/(?P<id>[0-9]+)/$', views.report),
# ]
#
# urlpatterns = [
#     re_path(r'blog/(page-(\d+)/)?$', views.blog_articles),
#     re_path(r'comments/(?:page-(?P<page_number>\d+)/)?$', views.comments),
#     re_path(r'^optional-args/(?P<year>[0-9]{4})/$', views.optional_args, {'foo': 'bar'}),
#     re_path(r'extra/', include(extra_patterns))
# ]
