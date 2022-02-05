from multiprocessing import context
from django.shortcuts import redirect, render

from courses.models import Course, Entry
from .forms import CourseForm, EntryForm

# Create your views here.


def index(request):
    """The home page for Learning Log.
    """
    return render(request, 'courses/index.html')


def courses(request):
    """Show all topics."""
    courses = Course.objects.order_by('course_created_datetime')
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)


def course(request, course_id):
    course = Course.objects.get(id=course_id)
    entries = course.entry_set.order_by('-date_added')
    context = {'course': course, 'entries': entries}
    return render(request, 'courses/course.html', context)


def exam(request):
    return render(request, 'courses/exam.html')


def new_course(request):
    if request.method != 'POST':
        form = CourseForm()
    else:
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:courses')
    context = {'form': form}
    return render(request, 'courses/new_course.html', context)


def new_entry(request, course_id):

    course = Course.objects.get(id=course_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.course = course
            new_entry.save()
            return redirect('courses:course', course_id=course_id)
    context = {'course': course, 'form': form}
    return render(request, 'courses/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    course = entry.course
