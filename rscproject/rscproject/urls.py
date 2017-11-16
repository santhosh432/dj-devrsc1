"""rscproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import django
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login

admin.autodiscover()

from onlinetestapp import views

# from django.contrib.auth import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #
    url(r'^check/$', views.check, name='check'),
    url(r'^$', views.home, name='home'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^registerpage/$', views.registration, name='register'),
    url(r'^adduser/$', views.add_user, name='adduser'),
    url(r'^loginverify/$', views.login_check, name='logincheck'),
    # url(r'^users/login/$', django.contrib.auth.views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^users/login/$', login, {'template_name': 'login.html'}, name='login'),
    #  url(r'^loginverify/options/$', views.admin_options, name='options'),

    url(r'^users/account/$', views.login_check, name='useraccount'),

    url(r'^loginverify/addtechnology/$', views.add_tech, name='addtech'),
    url(r'^loginverify/enterques/$', views.add_quest, name='addquest'),
    url(r'^loginverify/status/$', views.status, name='status'),
    url(r'^loginverify/techstatusup/$', views.statusupdate, name='statusupdate'),

    url(r'^loginverify/results/$', views.results, name='results'),
    url(r'^loginverify/edittech/$', views.edit_tech, name='edittech'),
    url(r'^loginverify/uptech/$', views.updatetechlist, name='updatetechlist'),
    url(r'^loginverify/questentry/$', views.questentry_tech, name='questentry'),
    url(r'^studenttest/$', views.student_first_page, name='student_first_page'),
    url(r'^starttest/$', views.starttest, name='starttest'),
    url(r'^acknowledgment/$', views.acknowledgment, name='acknowledgment'),
    url(r'^acknowledgmentfinal/$', views.acknowledgmentfinal, name='acknowledgmentfinal'),

]

#master one
# 3 added