from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class RegisterViewTests(TestCase):
    VALID_USER_DATA = {
        # 'first_name': 'first name',
        # 'last_name': 'last name',
        'email': 'test@user.com',
        'password': 'password',
        # 'password2': 'password',
    }

    def test_create_user_when_valid_data__expect_created_user(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.is_active)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

    def test_createsuperuser__when_valid_data__expect_superuser(self):
        admin_user = UserModel.objects.create_superuser(email='admin@user.com', password='admin123')
        self.assertEqual(admin_user.email, 'admin@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
