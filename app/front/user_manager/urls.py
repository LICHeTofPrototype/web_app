from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from front.user_manager.models import UserManager


urlpatterns = [
    path('', views.UserManagerView.as_view(model=UserManager), name='user_manager'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)