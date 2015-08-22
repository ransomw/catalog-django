from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True,
                                 **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    # fields
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=60
    )

    # custom manager
    objects = UserManager()

    # AbstractBaseUser class constants
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name'
    ] # /other/ than username

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """ True for login to admin app """
        return self.is_superuser
