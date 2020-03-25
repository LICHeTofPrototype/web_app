from django.contrib import admin
from django.urls import path
from front.account.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('v1/signin/', signin_api),
    path('v1/user_info/', user_info_api),
    path('signin/', login),
    path('signup/', create_account, name='create_account'),
]
