from django.contrib import admin

from courses.models import Content, Course, Entry, Homework

# Register your models here.
admin.site.register(Course)
admin.site.register(Entry)
admin.site.register(Homework)
admin.site.register(Content)
