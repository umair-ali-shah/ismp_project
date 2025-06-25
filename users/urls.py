from django.urls import path
from .views import dashboard_redirect

urlpatterns = [
    path('redirect/', dashboard_redirect, name='dashboard-redirect'),
]
