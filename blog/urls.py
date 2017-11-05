from django.conf.urls import url

from . import views
from .utils import ajax_required


urlpatterns = [
    url(r'^image/(?P<pk>[0-9]+)/$', views.ImageDetailView.as_view(), name='image_detail'),
    url(r'^image/create/$', views.ImageCreateView.as_view(), name='image_create'),
    url(r'^image-update/(?P<pk>[0-9]+)/$', views.EntryUpdateView.as_view(), name='image_update'),
    url(r'^create/$', views.EntryCreateView.as_view(), name='entry_create'),
    url(r'^list/$', views.EntryListView.as_view(), name='entry_list'),
    url(r'^search/$', ajax_required(views.JsonSearchView()), name='navbar_search'),
    url(r'^(?P<slug>[-\w]+)/$', views.EntryDetail.as_view(), name='entry_detail'),
]
