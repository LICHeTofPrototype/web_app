from django.contrib import admin
from django.urls import path
from users.views import signin, user_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/v1/signin', signin),
    path('/v1/signin', user_info),
]
