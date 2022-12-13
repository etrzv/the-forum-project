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

    def test_register__when_valid_data__expect_logged_in_user(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('register user'))
        self.assertTrue(user.is_authenticated)


'''
    def _create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user
        
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

'''