from turtle import title
from django.db import models

from django.conf import settings
# Create your models here.


class Course(models.Model):
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    course_name = models.CharField(max_length=200)
    course_description = models.CharField(max_length=200)
    #course_icon = models.CharField(max_length=200)
    course_created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.course_name


class Entry(models.Model):
    """Something specific learned about a topic."""
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content_title = models.CharField(max_length=200)
    content_description = models.CharField(max_length=200)
    content_created_datetime = models.DateTimeField(auto_now_add=True)
    content_updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.course)


class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    homework_title = models.CharField(max_length=200)
    homework_description = models.TextField(max_length=200)
    homework_instruction = models.TextField()
    homework_due_date = models.DateField(null=True)
    homework_created_datetime = models.DateTimeField(auto_now_add=True)
    homework_updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.course
