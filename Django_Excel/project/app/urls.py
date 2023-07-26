
from django.urls import path,include
from . import views
urlpatterns = [
    path('import/', views.importExcel,name='push_excel'),
    
]
