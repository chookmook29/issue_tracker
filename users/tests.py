from django.test import TestCase
from .models import CustomUser


class UserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="user", password="password")

    def test_user_fields(self):
        """CustomUser created has its correct default values"""
        user = CustomUser.objects.get(username="user")
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.contributions, 0)
        self.assertEqual(user.amount_comments, 0)
        self.assertEqual(user.last_name, "")

    def test_login_POST(self):
        response = self.client.post(
            "/login/", {"username": "user", "password": "password"}
        )
        self.assertEqual(response.status_code, 302)
