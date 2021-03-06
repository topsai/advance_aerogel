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
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('news/detail/<int:blog_id>/', views.news_detail, name='news_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('hongna/', views.hongna, name='hongna'),
    path('hongda/', views.hongda, name='hongda'),
    # 什么是气凝胶
    path('advance_aerogel/', views.advance_aerogel, name='advance_aerogel'),
    # 我们生产的气凝胶
    path('aerogels_we_provide/', views.aerogels_we_provide, name='aerogels_we_provide'),
    # 气凝胶工业的发展
    path('advance_aerogel_grow/', views.advance_aerogel_grow, name='advance_aerogel_grow'),
]
