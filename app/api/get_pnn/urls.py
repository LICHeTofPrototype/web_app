from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:user_id>/<int:measurement_id>/<int:request_index>/', views.GetPnnAPI.as_view(), name='get-pnn'),
    #path('<str:requestType>/', views.pnnResult, name='pnnReult'),    
]
urlpatterns = format_suffix_patterns(urlpatterns)