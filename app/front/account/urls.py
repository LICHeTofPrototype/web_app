from django.contrib import admin
from . import views
from django.urls import path
from front.account.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('v1/signin/', signin_api),
    path('v1/user_info/', user_info_api),
    path('signin/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
    path('show/', user_show, name='user_show'),
]
