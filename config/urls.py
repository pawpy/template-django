from django.contrib import admin
from django.urls import path

from visits import views

urlpatterns = [
    path("", views.index),
    path("health", views.health),
    path("admin/", admin.site.urls),
]
