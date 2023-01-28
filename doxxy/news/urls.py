from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name="all"),
    path('news/<slug:news_number_slug>', views.single_news, name='each_news_page'),
]


