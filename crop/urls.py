"""crop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admins import views as a
from users import views as u

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', a.index, name='index'),
    path('about', a.about, name='about'),
    path('contact', a.contact, name='contact'),
    path('alogin', a.alogin, name='alogin'),
    path('dashboard', a.dashboard, name='dashboard'),
    path('svm', a.svm, name='svm'),
    path('tcn', a.tcn, name='tcn'),

    path('ulogin', u.ulogin, name='ulogin'),
    path('register', u.register, name='register'),
    path('udashboard', u.udashboard, name='udashboard'),
    path('prediction', u.prediction, name='prediction'),
    
]
