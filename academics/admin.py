from django.contrib import admin
from .models import Class, Section, Subject, TeacherAssignment, Timetable, Attendance

admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(TeacherAssignment)
admin.site.register(Timetable)
admin.site.register(Attendance)