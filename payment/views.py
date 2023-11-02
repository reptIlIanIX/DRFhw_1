from django.shortcuts import render

from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer