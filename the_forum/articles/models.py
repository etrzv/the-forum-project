from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


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

    # auto_now: changes on creation and modification.
    # auto_now_add: changes once on creation only.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Search, Engine Optimisation
    # If the field is also unique, though, you'll have to use null=True to prevent multiple empty strings
    # from failing the uniqueness check
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        # the form does not require a value but the DB does
    )
    # null=True,
    # blank=False,
    # the form requires it, the DB does not - for values from users that are not required by the business logic

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

    def __str__(self):
        return self.title
