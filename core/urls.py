from django.urls import path
from .views import (
    admin_dashboard,
    teacher_dashboard,
    student_dashboard,
    parent_dashboard,
)

urlpatterns = [
    path('admin-dashboard/', admin_dashboard),
    path('teacher-dashboard/', teacher_dashboard),
    path('student-dashboard/', student_dashboard),
    path('parent-dashboard/', parent_dashboard),
]
