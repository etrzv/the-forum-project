from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from the_forum.accounts.models import Profile

UserModel = get_user_model()


class SignInViewTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'first name',
        'last_name': 'last name',
        'username': 'test_username',
        'email': 'test@user.com',
        'password1': 'password',
        'password2': 'password',
    }

    def test_sign_up__when_valid_data__expect_logged_in_user(self):
        response = self.client.post(
            reverse('login user'),
            data=self.VALID_USER_DATA,
        )

        self.assertEqual(self.VALID_USER_DATA['email'], response.context['user'].username)

