from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionCreateAPIView(generics.CreateAPIView):
    quaryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer, *args, **kwargs):
        subscription = serializer.save()  # получаю подписку
        subscription.user = self.request.user  # сохраняю в базе юзера
        course_pk = self.kwargs.get('pk')  # сохраняю pk
        subscription.course = Course.objects.get(pk=course_pk)  # достаю нужную подписку
        subscription.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
