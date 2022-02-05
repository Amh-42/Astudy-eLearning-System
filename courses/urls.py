from django.urls import path
from . import views
app_name = 'courses'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course, name='course'),
    path('new_course/', views.new_course, name='new_course'),
    path('new_entry/<int:course_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
