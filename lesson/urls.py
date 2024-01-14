from django.urls import path

from lesson.apps import LessonsConfig
from lesson.views import LessonDetailView, LessonListView, LessonCreateView, LessonUpdateView, LessonDestroyView

app_name = LessonsConfig.name

urlpatterns = [path('', LessonListView.as_view(), name='lesson-list'),
               path('<int:pk>', LessonDetailView.as_view(), name='lesson-detail'),
               path('<int:pk>/update/', LessonUpdateView.as_view()),
               path('create/', LessonCreateView.as_view(), name='lesson-create'),
               path('<int:pk>/delete', LessonDestroyView.as_view()),

               ]
