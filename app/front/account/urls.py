from django.contrib import admin
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]
