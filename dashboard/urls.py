from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard-bar'),
    path('dashboard-pie', views.pie, name='dashboard-pie'),
    path('dashboard-line', views.line, name='dashboard-line'),
    path('dashboard-doughnut', views.doughnut, name='dashboard-doughnut'),
]
