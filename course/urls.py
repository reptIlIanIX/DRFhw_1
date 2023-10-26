from django.urls import path, include
from rest_framework import routers

from course.apps import CourseConfig
from course.views import CourseViewSet

app_name = CourseConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [] + router.urls
