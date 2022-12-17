from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from the_forum.articles.forms import ArticleCreateForm, ArticleEditForm, ArticleDeleteForm
from the_forum.articles.models import Article


class ArticleFormTests(TestCase):
    VALID_ARTICLE_DATA = {
        'title': 'Test',
        'content': 'TestContent',
    }

    def test_article_create_form__with_valid_data__expect_created_article(self):
        form = ArticleCreateForm(self.VALID_ARTICLE_DATA)
        self.assertTrue(form.is_valid())
        self.assertIsNotNone(form)

    def test_article_edit_form__with_invalid_data__expect_edited_article(self):
        form = ArticleCreateForm(self.VALID_ARTICLE_DATA)
        new_data = {
            'title': 'NewTitle',
            'content': 'NewContent',
        }
        edit_form = ArticleEditForm(new_data)
        self.assertTrue(edit_form.is_valid())
        self.assertNotEqual(form, edit_form)

    def test_article_delete_form__expect_no_article(self):
        article = ArticleCreateForm(self.VALID_ARTICLE_DATA)
        delete_form = ArticleDeleteForm(article)

        self.assertTrue(delete_form.is_valid())


