from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from course.models import Course
from lesson.models import Lesson
from subscription.models import Subscription
from users.models import User
from rest_framework.test import APITestCase


# Create your tests here.
class LessonTestCase(APITestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.user = User.objects.create(
            username='admin',
            is_active=True
        )
        self.user.set_password('1234')
        self.user.save()

        get_token = reverse('user:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'username': 'admin', 'password': '1234'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.course = Course.objects.create(
            name='test_course',
            description='test'

        )

        self.lesson = Lesson.objects.create(
            name='test',
            description="test",

            course=self.course
        )

    # def test_get_list(self):
    #         """Test for getting list of lessons"""
    #
    #         response = self.client.get(
    #             reverse('lesson:lesson-list')
    #         )
    #
    #         self.assertEqual(
    #             response.status_code,
    #             status.HTTP_200_OK
    #         )
    #
    #         self.assertEqual(
    #             response.json(),
    #             {"count": 2, "next": None, "previous": None, "results": [
    #                 {"id": 5, "name": "colonial history", "description": "to know your country", "image": None,
    #                  "link": None, "course": 12, "owner": 1},
    #                 {"id": 6, "name": "ethnic cuisine", "description": "to know your country", "image": None, "link": None,
    #                  "course": 13, "owner": 1}]}
    #
    #         )
    def test_lesson_create(self):
            """Test lesson creating"""

            data = {
                "name": "test",
                "description": "test",
                "course": self.course,
            }

            response = self.client.post(
                reverse('lesson:lesson-create'),
                data=data
            )
            print(response)

            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED
            )

            self.assertEqual(
                Lesson.objects.all().count(),
                2
            )
