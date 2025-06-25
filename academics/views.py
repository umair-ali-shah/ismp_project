from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Student
from academics.models import Attendance, Class, Section
from datetime import date
from django.contrib import messages

@login_required
def mark_attendance(request):
    selected_class = request.GET.get('class')
    selected_section = request.GET.get('section')
    today = date.today()
    students = None
    attendance_data = {}

    if selected_class and selected_section:
        students = Student.objects.filter(
            student_class__id=selected_class,
            section__id=selected_section
        ).select_related('user')

        # Fetch any existing attendance records for today
        existing_attendance = Attendance.objects.filter(
            student__in=students,
            date=today
        )

        attendance_data = {att.student.id: att.status for att in existing_attendance}

    if request.method == 'POST':
        total = int(request.POST.get('total_students'))
        for i in range(total):
            student_id = request.POST.get(f'student_id_{i}')
            status = request.POST.get(f'status_{i}')
            student = Student.objects.get(id=student_id)

            # Update or create attendance for today
            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={
                    'status': status,
                    'recorded_by': request.user
                }
            )
        messages.success(request, "✅ Attendance has been saved (new or updated).")
        return redirect(f"/mark-attendance/?class={selected_class}&section={selected_section}")

    return render(request, 'academics/mark_attendance.html', {
        'classes': Class.objects.all(),
        'sections': Section.objects.all(),
        'students': students,
        'attendance_data': attendance_data,
        'selected_class': selected_class,
        'selected_section': selected_section,
        'total': students.count() if students else 0
    })
