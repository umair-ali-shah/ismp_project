from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from academics.models import Class, Section
from academics.models import Attendance
from datetime import date

def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return redirect('redirect')

    total_students = User.objects.filter(role='STUDENT').count()
    total_teachers = User.objects.filter(role='TEACHER').count()
    total_parents = User.objects.filter(role='PARENT').count()
    total_classes = Class.objects.count()
    total_sections = Section.objects.count()
    attendance_today = Attendance.objects.filter(date=date.today()).count()

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_parents': total_parents,
        'total_classes': total_classes,
        'total_sections': total_sections,
        'attendance_today': attendance_today,
    }
    return render(request, 'core/admin_dashboard.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'STUDENT'  # Default role (adjust as needed)
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def home_view(request):
    return render(request, 'core/home.html')

@login_required
def redirect_view(request):
    user = request.user

    if user.role == 'ADMIN':
        return redirect('admin-dashboard')
    elif user.role == 'TEACHER':
        return redirect('teacher-dashboard')
    elif user.role == 'STUDENT':
        return redirect('student-dashboard')
    elif user.role == 'PARENT':
        return redirect('parent-dashboard')
    else:
        return redirect('default-dashboard')

@login_required
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

@login_required
def parent_dashboard(request):
    return render(request, 'core/parent_dashboard.html')
