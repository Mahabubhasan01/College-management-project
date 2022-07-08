from . import views
from django.urls import path, include
urlpatterns = [
    path('hod/', include('principle.urls')),
    path('teachers/', include('teachers.urls')),
    path('students', include('students.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('studentform/', views.student_form ,name='studentform')
]
