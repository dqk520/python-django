#coding=UTF-8
"""mysite URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from mysite.views import *
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
	('^time/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^text/$', book_list),
	(r'^ttt/$', display_meta),
	(r'^search-form/$', search_form),
	(r'^search/$', search),
	(r'^book/$', book_list),
	(r'^home/$', home),	
	(r'^home2/$', home2),
	(r'^admin/', include(admin.site.urls)),	
)

