from rest_framework import serializers
from .models import Teachers, Organizer, Groups, Students

class OrganizerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        exclude = ("password",)

class OrganizerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = "__all__"

class TeachersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = ("name", "email", "organizer")


class TeacherDetailSerializer(serializers.ModelSerializer):
    organizer = OrganizerDetailSerializer()

    class Meta:
        model = Teachers
        exclude = ("password",)

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class GroupListSerializer(serializers.ModelSerializer):
    organizer = OrganizerDetailSerializer()

    class Meta:
        model = Groups
        fields = "__all__"



class StudentListSerializer(serializers.ModelSerializer):
    group = GroupListSerializer()

    class Meta:
        model = Students
        exclude = ("password", )