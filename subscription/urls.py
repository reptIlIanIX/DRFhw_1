from django.urls import path

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionDestroyAPIView, SubscriptionCreateAPIView

app_name = SubscriptionConfig.name

urlpatterns = [path('course/<int:pk>/createsub/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
               path('course/<int:pk>/deletesub/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'), ]
