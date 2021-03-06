"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from capp import views as capp_views
from cauth import views as cauth_views

urlpatterns = [
    url(r'^$', capp_views.home, name='home'),
    url(r'^login$', cauth_views.login, name='login'),
    url(r'^logout$', cauth_views.logout, name='logout'),
    url(r'^catalog/', include('capp.urls', namespace='capp')),
    url(r'^admin/', include(admin.site.urls)),
]
