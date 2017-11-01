"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import blog.urls
from blog.views import JsonSearchView


urlpatterns = [
    url(r'^search/', JsonSearchView(), name='navbar_search'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^blog/$', TemplateView.as_view(template_name="blog.html"), name='blog'),
    url(r'^feedback/$', TemplateView.as_view(template_name="feedback.html"), name='feedback'),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^', include(blog.urls)),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
