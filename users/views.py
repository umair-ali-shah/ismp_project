from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_redirect(request):
    role = request.user.role

    if role == 'ADMIN':
        return redirect('/admin-dashboard/')
    elif role == 'TEACHER':
        return redirect('/teacher-dashboard/')
    elif role == 'STUDENT':
        return redirect('/student-dashboard/')
    elif role == 'PARENT':
        return redirect('/parent-dashboard/')
    else:
        return redirect('/login/')
