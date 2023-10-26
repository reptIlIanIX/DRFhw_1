from django.urls import path

from lesson.views import LessonDetailView, LessonListView, LessonCreateView, LessonUpdateView, LessonDestroyView

urlpatterns = [path('', LessonListView.as_view()),
               path('<int:pk>', LessonDetailView.as_view()),
               path('<int:pk>/update/', LessonUpdateView.as_view()),
               path('create/', LessonCreateView.as_view()),
               path('<int:pk>/delete', LessonDestroyView.as_view()),

               ]
