from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from core.validators import validate_only_letters, validate_file_max_size_in_mb
from the_forum.accounts.managers import AppUserManager

'''
1. Create model extending classes 
2. Configure this model in settings.py 
3. Create user manager which the model is going to use 

the AbstractBaseUser gives us the basic functions needed for a user - keeps passwords, last login, password save etc
the PermissionsMixin has 3 properties that allows us to make our users in the class able to use administration
this information is needed only for the login:
'''

# TODO:
# django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'accounts.AppUser'
# that has not been installed
# UserModel = get_user_model()


class AppUser(AbstractBaseUser, PermissionsMixin):
    EMAIL_MAX_LEN = 15

    # email
    # password
    # is_staff
    # is_superuser

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        unique=True,
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    # creating a custom manager that is overridden here - from the UserManager base class
    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    # first_name
    # last_name
    # profile_image

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        validators=(validate_file_max_size_in_mb, ),
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
