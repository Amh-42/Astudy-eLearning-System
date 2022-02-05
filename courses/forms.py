from django import forms
from .models import Course, Entry


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']
        labels = {'course_name': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['course_name']
        labels = {'course_name': 'Entry:'}
        widgets = {'course_name': forms.Textarea(attrs={'cols': 80})}
