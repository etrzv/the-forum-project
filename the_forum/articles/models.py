from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


UserModel = get_user_model()


class Article(models.Model):
    MAX_LEN_TITLE = 100
    MAX_LEN_CONTENT = 20000

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )

    content = models.CharField(
        max_length=MAX_LEN_CONTENT,
        null=False,
        blank=False,
    )

    photo = models.URLField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.title}')

        return super().save(*args, **kwargs)
