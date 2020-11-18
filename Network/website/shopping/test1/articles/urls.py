
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name="list"),
    path('<slug>',views.article_detail,name="detail"),
]
