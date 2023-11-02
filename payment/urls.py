from django.urls import path, include
from rest_framework import routers

from course.apps import CourseConfig
from course.views import CourseViewSet
from payment.apps import PaymentConfig
from payment.views import PaymentViewSet

app_name = PaymentConfig.name

router = routers.DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='paymnet')

urlpatterns = [] + router.urls