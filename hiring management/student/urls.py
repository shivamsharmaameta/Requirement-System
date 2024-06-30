from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('login/', views.student_login, name='login'),
]
