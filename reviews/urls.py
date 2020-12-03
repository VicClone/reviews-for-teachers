from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("teachers/", views.TeachersListView.as_view()),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view()),
    path("teacher/", views.TeacherCreateView.as_view()),

    path("organizer/", views.OrganizerCreateView.as_view()),

    path("groups/", views.GroupListView.as_view()),
    path("students/", views.StudentListView.as_view()),
]