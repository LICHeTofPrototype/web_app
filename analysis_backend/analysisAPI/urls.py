from django.urls import path
from analysisAPI import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:requestType>/', views.pnnResult, name='pnnReult'),    
]