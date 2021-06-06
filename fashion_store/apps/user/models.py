from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phone_field import PhoneField

from utils.abstract_models import CreateUpdateModel


class NewUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        return self.create_user(email, password, **extra_kwargs)


class UserModel(AbstractBaseUser, PermissionsMixin, CreateUpdateModel):
    email = models.EmailField(max_length=100, verbose_name='Email',
                              unique=True)
    first_name = models.CharField(max_length=20, verbose_name='Name')
    phone = PhoneField(blank=True, help_text='Contact phone number', null=True)
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    city = models.CharField(max_length=100, verbose_name='City', blank=True)
    state = models.CharField(max_length=100, verbose_name='State', blank=True)
    zip = models.CharField(max_length=100, verbose_name='ZIP', blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
