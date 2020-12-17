from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class OrganizersListView(APIView):
  def get(self, request):
    organizer = Organizer.objects
    if request.GET.get('login') and request.GET.get('password'):
      organizer = Organizer.objects.filter(email=request.GET.get('login'), password=request.GET.get('password'))

    if request.GET.get('id'):
      organizer = Organizer.objects.filter(id=request.GET.get('id'))

    serializer = OrganizerDetailSerializer(organizer, many=True)

    return Response(serializer.data)

class OrganizerCreateView(APIView):
  def post(self, request):
    organizer = OrganizerCreateSerializer(data=request.data)

    if organizer.is_valid():
      organizer.save()

    return Response(organizer.data, status=201)

class TeachersListView(APIView):
  def get(self, request):
    teachers = Teachers.objects.filter(organizer=request.GET.get('id'))

    if request.GET.get('login') and request.GET.get('password'):
      teachers = Teachers.objects.filter(email=request.GET.get('login'), password=request.GET.get('password'))

    serializer = TeachersListSerializer(teachers, many=True)

    return Response(serializer.data)


class TeacherDetailView(APIView):
  def get(self, request, pk):
    teacher = Teachers.objects.get(id=pk)
    serializer = TeacherDetailSerializer(teacher)

    return Response(serializer.data)


class TeacherCreateView(APIView):
  def post(self, request):
    teacher = TeacherCreateSerializer(data=request.data)

    if teacher.is_valid():
      teacher.save()

    return Response(teacher.data, status=201)


class UpdateGroupsTeacherViews(APIView):
  def post(self, request):
    serializer = UpdateGroupTeacherSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=201)

    else: 
      return Response(status=400)


class GroupListView(APIView):
  def get(self, request):
    groups = Groups.objects

    if request.GET.get('organizer'):
      groups = Groups.objects.filter(organizer=request.GET.get('organizer'))

    serializer = GroupListSerializer(groups, many=True)

    return Response(serializer.data)


class GroupCreateView(APIView):
  def post(self, request):
    group = GroupCreateSerializer(data=request.data)

    if group.is_valid():
      group.save()

    return Response(status=201)


class StudentListView(APIView):
  def get(self, request):
    students = Students.objects

    if request.GET.get('login') and request.GET.get('password'):
      students = Students.objects.filter(email=request.GET.get('login'), password=request.GET.get('password'))

    serializer = StudentListSerializer(students, many=True)

    return Response(serializer.data)

class StudentCreateView(APIView):
  def post(self, request):
    student = StudentCreateSerializer(data=request.data)

    if student.is_valid():
      student.save()

    return Response(status=201)

class StudentDetailView(APIView):
  def get(self, request, pk):
    student = Students.objects.get(id=pk)
    serializer = StudentDetailSerializer(student)

    return Response(serializer.data)


class SubjectsListView(APIView):
  def get(self, request):
    subjects = Subjects.objects
    if request.GET.get('organizer'):
      subjects = Subjects.objects.filter(organizer=request.GET.get('organizer'))

    serializer = SubjectsListSerializer(subjects, many=True)

    return Response(serializer.data)

class SubjectCreateView(APIView):
  def post(self, request):
    subject = SubjectsListSerializer(data=request.data)

    if subject.is_valid():
      subject.save()

    return Response(status=201)


class ReviewsListView(APIView):
  def get(self, request):
    reviews = Reviews.objects

    if request.GET.get('group'):
      reviews = Reviews.objects.filter(group=request.GET.get('group'))

    serializer = ReviewsListSerializer(reviews, many=True)

    return Response(serializer.data)


class ReviewСreateView(APIView):
  def post(self, request):
    review = ReviewsListSerializer(data=request.data)

    if review.is_valid():
      review.save()

    return Response(status=201)


class AnswersListView(APIView):
  def get(self, request):
    answers = Answers.objects

    # if request.GET.get('student'):
    #   student = Answers.objects.filter(student=request.GET.get('student'))

    serializer = AnswersListSerializer(answers, many=True)

    return Response(serializer.data)

class AnswerCreateView(APIView):
  def post(self, request):
    answer = AnswersListSerializer(data=request.data)

    if answer.is_valid():
      answer.save()

    return Response(status=201)