"""advance_aerogel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.home_cn, name='home'),
    path('service/', views.service_cn, name='service'),
    path('about/', views.about_cn, name='about'),
    path('contact/', views.contact_cn, name='contact'),
    path('news/', views.news_cn, name='news'),
    path('news/detail/<int:blog_id>/', views.news_detail_cn, name='news_detail'),
    path('gallery/', views.gallery_cn, name='gallery'),
]
