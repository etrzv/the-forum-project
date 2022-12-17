from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from django.test import TestCase
from tests.utils.creation_utils import create_articles_for_user, create_article_likes_for_user_and_articles, \
    create_article_dislikes_for_user_and_articles
from the_forum.articles.models import Article
from the_forum.common.models import ArticleLike

UserModel = get_user_model()


class UserDetailsViewTests(TestCase):

    def test_article_likes__when_1_likes_are_given__expect_1_likes(self):
        user = UserModel.objects.create_user('test_email@ss.com', 'password1')
        article = create_articles_for_user(user, 1)
        given_likes_count = 1
        article_likes = create_article_likes_for_user_and_articles(given_likes_count, user, article)

        self.assertEqual(given_likes_count, article_likes)

    def test_article_likes__when_10_likes_are_given__expect_10_likes(self):
        user = UserModel.objects.create_user('test_email@ss.com', 'password1')
        article = create_articles_for_user(user, 1)
        given_likes_count = 10
        article_likes = create_article_likes_for_user_and_articles(given_likes_count, user, article)

        self.assertEqual(given_likes_count, article_likes)

    def test_article_dislikes__when_1_dislikes_are_given__expect_1_dislikes(self):
        user = UserModel.objects.create_user('test_email@ss.com', 'password1')
        article = create_articles_for_user(user, 1)
        given_dislikes_count = 1
        article_dislikes = create_article_dislikes_for_user_and_articles(given_dislikes_count, user, article)

        self.assertEqual(given_dislikes_count, article_dislikes)

    def test_article_dislikes__when_10_dislikes_are_given__expect_10_dislikes(self):
        user = UserModel.objects.create_user('test_email@ss.com', 'password1')
        article = create_articles_for_user(user, 1)
        given_dislikes_count = 10
        article_dislikes = create_article_dislikes_for_user_and_articles(given_dislikes_count, user, article)

        self.assertEqual(given_dislikes_count, article_dislikes)
