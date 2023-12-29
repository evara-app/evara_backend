from enum import Enum
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=300,
        unique=True,
        verbose_name="User Name",
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Is Staff",
        help_text="If Is Staff True This User Can Login Admin Panel",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="If Is Active True Means User In System",
    )
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="Date Joined")
    objects = CustomUserManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        if self.username:
            return self.username
        return f"User ID {self.id}"

    @property
    def is_admin(self):
        return self.is_superuser

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User's"


class Role(Enum):
    common = 1
    agent = 2
    admin = 5


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
        verbose_name="For User",
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Phone Number",
    )
    isd = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="ISD",
        help_text="International Subscriber Dialing For Iran: +98",
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name="Email",
    )
    full_name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Full Name",
    )
    role = models.PositiveSmallIntegerField(
        default=1, verbose_name="Role", help_text="1:common 2:agent 5:admin"
    )
    avatar = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Avatar",
        help_text="Avatar Image Link",
    )
    real_estate_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Real Estate Name",
        help_text="If User Have Real Estate name",
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profile's"


class Otp(models.Model):
    uuid_token = models.CharField(
        max_length=100,
        verbose_name="Token",
        help_text="For Found Password In System",
    )
    password = models.CharField(
        max_length=5,
        verbose_name="Password",
        help_text="Generated Password From Server",
    )
    email = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Email",
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Phone Number",
    )
    isd = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="ISD",
        help_text="International Subscriber Dialing For Iran: +98",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Create Time",
        help_text="When Object Is Created",
    )

    class Meta:
        verbose_name = "Otp Data"
        verbose_name_plural = "Otp Data"
