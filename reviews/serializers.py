from rest_framework import serializers
from .models import Teachers, Organizer, Groups, Students, Subjects, Reviews, Answers

class OrganizerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = "__all__"

class OrganizerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = "__all__"

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class GroupListSerializer(serializers.ModelSerializer):
    organizer = OrganizerDetailSerializer()

    class Meta:
        model = Groups
        fields = "__all__"

class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class StudentDetailSerializer(serializers.ModelSerializer):
    group = GroupListSerializer()

    class Meta:
        model = Students
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        exclude = ("password", )


class SubjectsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = "__all__"

class TeachersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = ("id", "name", "email", "organizer")


class TeacherDetailSerializer(serializers.ModelSerializer):
    organizer = OrganizerDetailSerializer()
    groups = GroupListSerializer(many=True)
    subjects = SubjectsListSerializer(many=True)
    my_field = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, foo):
      return foo.name == "bar"

    class Meta:
        model = Teachers
        exclude = ("password",)


class UpdateGroupTeacherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teachers
        fields = ("id", "groups")

    def create(self, validated_data):
        teacher = Teachers.objects.update_or_create(
            id=validated_data.get('id', None),
            defaults={'groups': validated_data.get("groups")}
        )

        return teacher


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = "__all__"

class ReviewsListSerializer(serializers.ModelSerializer):
    teacher = TeachersListSerializer()
    subject = SubjectsListSerializer()
    group = GroupListSerializer()

    class Meta:
        model = Reviews
        fields = "__all__"


class AnswersListSerializer(serializers.ModelSerializer):
    review = ReviewsListSerializer()
    student = StudentListSerializer()

    class Meta:
        model = Answers
        fields = "__all__"

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"