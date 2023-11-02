from rest_framework import serializers

from course.models import Course
from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson_course = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'lesson_count', 'lesson_course']

    def get_lesson_count(self, lesson):
        return lesson.lesson_set.count()
