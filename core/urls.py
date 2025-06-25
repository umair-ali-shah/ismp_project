from django.urls import path
from .views import (
    redirect_view,
    admin_dashboard,
    teacher_dashboard,
    student_dashboard,
    parent_dashboard,
    signup_view
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('redirect/', redirect_view, name='redirect'),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('teacher/dashboard/', teacher_dashboard, name='teacher-dashboard'),
    path('student/dashboard/', student_dashboard, name='student-dashboard'),
    path('parent/dashboard/', parent_dashboard, name='parent-dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup_view, name='signup'),
]
