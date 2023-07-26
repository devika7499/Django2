from django.urls import path
from data_api.views import get_annual_data

app_name = 'data_api'


urlpatterns = [
    path('data', get_annual_data, name='get_annual_data'),
]
