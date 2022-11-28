from django.conf import settings
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

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # called when createsuperuser 
    # relates to the _create_user function in the UserManager

    # creating a custom manager that is overridden here - from the UserManager base class
    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    USERNAME_MAX_LEN = 25

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        # null=True,
        # blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
        # null=True,
        # blank=True,
    )

    username = models.CharField(
       max_length=USERNAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        validators=(validate_file_max_size_in_mb, ),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        # TODO:
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

'''
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

'''