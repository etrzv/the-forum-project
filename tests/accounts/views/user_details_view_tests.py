from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_articles_for_user, create_article_likes_for_user_and_articles

UserModel = get_user_model()


class UserDetailsViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'email@abv.com',
        'password': 'password',
    }

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_has_created_articles__expect_articles(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        articles_count = 5
        create_articles_for_user(user, count=articles_count)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(len(response.context['articles']), articles_count)

    def test_user_details__when_no_articles__expect_empty_articles(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['articles'])
