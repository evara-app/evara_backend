from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from apps.utilities.messages import UserMessages


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        from .validations import UserValidation

        email = extra_fields.get("email")
        phone_number = extra_fields.get("phone_number")
        if UserValidation.check_email_exists(
            email=email
        ) or UserValidation.check_phone_exists(phone_number=phone_number):
            raise ValueError(UserMessages.user_exists.value)
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(username=username, password=password, **extra_fields)
