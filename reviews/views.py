from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class OrganizerCreateView(APIView):
  def post(self, request):
    organizer = OrganizerCreateSerializer(data=request.data)

    if organizer.is_valid():
      organizer.save()

    return Response(status=201)

class TeachersListView(APIView):
  def get(self, request):
    teachers = Teachers.objects

    serializer = TeachersListSerializer(teachers, many=True)

    return Response(serializer.data)


class TeacherDetailView(APIView):
  def get(self, request, pk):
    teacher = Teachers.objects.get(id=pk)
    serializer = TeachersListSerializer(teacher)

    return Response(serializer.data)


class TeacherCreateView(APIView):
  def post(self, request):
    teacher = TeacherCreateSerializer(data=request.data)

    if teacher.is_valid():
      teacher.save()

    return Response(status=201)


class GroupListView(APIView):
  def get(self, request):
    groups = Groups.objects

    serializer = GroupListSerializer(groups, many=True)

    return Response(serializer.data)


class StudentListView(APIView):
  def get(self, request):
    students = Students.objects

    serializer = StudentListSerializer(students, many=True)

    return Response(serializer.data)