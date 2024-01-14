from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [path('', UserListView.as_view(), name='user-list'),
               path('<int:pk>', UserDetailView.as_view(), name='user-get'),
               path('<int:pk>/update/', UserUpdateView.as_view(),name='user-update'),
               path('create/', UserCreateView.as_view(), name='user-create'),
               path('<int:pk>/delete', UserDestroyView.as_view(), name='user-delete'),
               path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
               ]
