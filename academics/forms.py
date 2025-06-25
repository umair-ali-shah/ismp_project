from django import forms
from users.models import Student
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status']

AttendanceStatusChoices = Attendance._meta.get_field('status').choices

class AttendanceEntryForm(forms.Form):
    student_id = forms.IntegerField(widget=forms.HiddenInput())
    student_name = forms.CharField(disabled=True)
    status = forms.ChoiceField(choices=AttendanceStatusChoices)
