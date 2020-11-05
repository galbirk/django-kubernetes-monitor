from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name='monitor-login'),
    path('monitor/', views.monitor,name='monitor-monitor')
]