from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from the_forum.articles.models import Article


class ArticleViewTests(TestCase):
    VALID_ARTICLE_DATA = {
        'title': 'Test',
        'content': 'TestContent',
    }

    def test_create_article_when_valid_data__expect_created_article(self):
        article = Article.objects.create(**self.VALID_ARTICLE_DATA)
        self.assertIsNotNone(article)


    # def test_createsuperuser__when_valid_data__expect_superuser(self):
    #     admin_user = UserModel.objects.create_superuser(email='admin@user.com', password='admin123')
    #     self.assertEqual(admin_user.email, 'admin@user.com')
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)
    #     try:
    #         self.assertIsNone(admin_user.username)
    #     except AttributeError:
    #         pass
