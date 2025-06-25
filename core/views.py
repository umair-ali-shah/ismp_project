from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return HttpResponse("🎯 Admin Dashboard")

@login_required
def teacher_dashboard(request):
    return HttpResponse("📘 Teacher Dashboard")

@login_required
def student_dashboard(request):
    return HttpResponse("📚 Student Dashboard")

@login_required
def parent_dashboard(request):
    return HttpResponse("👨‍👩‍👧‍👦 Parent Dashboard")
