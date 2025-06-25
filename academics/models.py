from django.db import models
from django.conf import settings

class Class(models.Model):
    name = models.CharField(max_length=50)  # e.g., Grade 1

    def __str__(self):
        return self.name

class Section(models.Model):
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=5)  # e.g., A, B, C

    def __str__(self):
        return f"{self.class_ref.name} - {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)  # e.g., Science
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class TeacherAssignment(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'})
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'section', 'subject')

    def __str__(self):
        return f"{self.teacher.email} → {self.section} → {self.subject.name}"

DAYS_OF_WEEK = [
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
]

class Timetable(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'})
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['day', 'start_time']
        unique_together = ('section', 'day', 'start_time')

    def __str__(self):
        return f"{self.section} | {self.subject.name} | {self.day} {self.start_time}-{self.end_time}"

ATTENDANCE_STATUS = [
    ('PRESENT', 'Present'),
    ('ABSENT', 'Absent'),
    ('LEAVE', 'Leave'),
]

class Attendance(models.Model):
    student = models.ForeignKey("users.Student", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS)
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 'TEACHER'}
    )

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.user.email} - {self.date} - {self.status}"