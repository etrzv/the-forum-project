from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User, AbstractUser
from django.core import validators
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
    EMAIL_MAX_LEN = 35

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    # auto_now: changes on creation and modification.
    # auto_now_add: changes once on creation only.
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # called when createsuperuser 
    # relates to the _create_user function in the UserManager

    # creating a custom manager that is overridden here - from the UserManager base class
    objects = AppUserManager()

    # TODO: does not work when registering
    # def get_profile(self):
    #     return Profile.objects.get(user_id=self.pk)
    #
    # def get_first_name(self):
    #     profile = self.get_profile()
    #     return profile.first_name
    #
    # def get_username(self):
    #     profile = self.get_profile()
    #     return profile.username


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    USERNAME_MAX_LEN = 25

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        null=False,
        blank=False,
        unique=True,
    )

    profile_image = models.ImageField(
        validators=(validate_file_max_size_in_mb,),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
