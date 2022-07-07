from django.urls import path,include
urlpatterns = [
    path('hod/',include('principle.urls')),
    path('teachers/',include('teachers.urls')),
    path('students/',include('students.urls')),
]
