
from django.contrib import admin
from django.urls import path

from .views import home_view, about_view

urlpatterns = [
    path("", home_view),   #index page
    path("hello-world/", home_view),
    path('admin/', admin.site.urls),
    path("about/", about_view),
]
