from django.urls import path
from .views import mark_attendance
from django.http import HttpResponse

urlpatterns = [
    path('mark-attendance/', mark_attendance, name='mark-attendance'),
    path('attendance-success/', lambda request: HttpResponse("✅ Attendance saved!"), name='attendance-success')
]
