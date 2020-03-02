from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.HeartBeatAPI.as_view(), name='heart-beat'),
    #path('<str:requestType>/', views.pnnResult, name='pnnReult'),    
]
urlpatterns = format_suffix_patterns(urlpatterns)