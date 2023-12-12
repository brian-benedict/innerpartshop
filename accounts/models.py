# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserProfileManager(BaseUserManager):
    pass  # You can add custom manager methods here if needed

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)  # Add 'is_staff' if needed
    is_active = models.BooleanField(default=True)  # Add 'is_active' if needed
    # other fields...

    # Add related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_profiles'  # Unique related name for groups
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_profiles'  # Unique related name for user_permissions
    )

    USERNAME_FIELD = 'username'

    # You can add additional fields and methods as needed
