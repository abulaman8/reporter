from django.urls import path
from . import views


urlpatterns = [
    # path('', views.base, name='home'),
    path('', views.index, name='home'),
    # path('student/', views.index, name='student_dashboard'),
    # path('parent/', views.index, name='parent_dashboard'),
    # path('admin/', views.index, name='admin_dashboard'),
    # path('faculty/', views.index, name='faculty_dashboard'),
    # path('coach/', views.index, name='coach_dashboard'),
    path('report/', views.view_report, name='view_report'),
]
