from django.urls import path
from .views import StudentListView, LandingView, StudentDetailView, Student

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path("", LandingView.as_view(), name="landing"),
    path("",StudentDetailView.as_view(), name="student_detail"),
]