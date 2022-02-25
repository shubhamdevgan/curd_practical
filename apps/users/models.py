from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserModelManager
from .choices import ShiftChoices
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    '''
        Default User Model for project
    '''
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(unique=True,)
    password = models.CharField(max_length=246)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    total_experience = models.CharField(max_length=30, null=True, blank=True)
    work_shift = models.CharField(
        max_length=5, choices=ShiftChoices, null=True, blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Signup done On')

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["username", "password"]
    objects = UserModelManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        '''
            Return Full Name of the User
        '''
        return f'{self.first_name} {self.last_name}'
