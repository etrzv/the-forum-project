from django.contrib.auth import get_user_model
from django.db import models
from the_forum.articles.models import Article


UserModel = get_user_model()


class ArticleLike(models.Model):
    # Articles' field for likes is named `{NAME_OF_THIS_MODEL.lower()}_set`
    # likes_count': photo.photolike_set.count(),

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class ArticleDislike(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class ArticleBookmark(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class ArticleComment(models.Model):
    MAX_LEN_TEXT = 600

    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        null=False,
        blank=False,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class CommentLike(models.Model):
    comment = models.ForeignKey(
        ArticleComment,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class CommentDislike(models.Model):
    comment = models.ForeignKey(
        ArticleComment,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
