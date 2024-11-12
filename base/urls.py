from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('report/', views.view_report, name='view_report'),
    path('summary/', views.view_suumary, name='view_summary'),
]
