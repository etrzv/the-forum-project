from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from the_forum.articles.models import Article

UserModel = get_user_model()


class ArticleViewTests(TestCase):
    VALID_ARTICLE_DATA = {
        'title': 'Test',
        'content': 'TestContent',
    }

    def test_create_article_when_valid_data__expect_created_article(self):
        user = UserModel.objects.create_user('test_email@ss.com', 'password1')
        article = Article(
            title='Test',
            content='TestContent',
            user_id=user.pk,
        )
        article.save()
        response = self.client.post(reverse_lazy('add article'))
        self.assertIsNotNone(article)
        self.assertEqual(article.title, 'Test')
        self.assertEqual(article.content, 'TestContent')
        self.assertEqual(article.user_id, user.pk)
        self.assertEqual(response.status_code, 302)



