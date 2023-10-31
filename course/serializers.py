from rest_framework import serializers

from course.models import Course
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['name', 'description', 'lesson_count']

    def get_lesson_count(self, lesson):
        return lesson.lesson_set.count()
