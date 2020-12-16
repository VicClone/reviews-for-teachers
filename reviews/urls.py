from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("teachers/", views.TeachersListView.as_view()),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view()),
    path("teacher/", views.TeacherCreateView.as_view()),

    path("organizer/", views.OrganizerCreateView.as_view()),
    path("organizers/", views.OrganizersListView.as_view()),

    path("groups/", views.GroupListView.as_view()),
    path("group/", views.GroupCreateView.as_view()),

    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>/", views.StudentDetailView.as_view()),
    path("student/", views.StudentCreateView.as_view()),
    
    path("subjects/", views.SubjectsListView.as_view()),
    path("subject/", views.SubjectCreateView.as_view()),

    path("reviews/", views.ReviewsListView.as_view()),
    path("review/", views.ReviewСreateView.as_view()),

    path("answers/", views.AnswersListView.as_view()),
    path("answer/", views.AnswerCreateView.as_view()),
]