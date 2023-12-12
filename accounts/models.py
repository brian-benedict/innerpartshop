# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from shops.models import Shop  # Import the Shop model




class UserProfileManager(BaseUserManager):
    pass  # You can add custom manager methods here if needed

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)  # Add 'is_staff' if needed
    is_active = models.BooleanField(default=True)  # Add 'is_active' if needed
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True, related_name='userprofile')

    # other fields...

    user = models.OneToOneField(
            'auth.User',  # Or replace 'auth.User' with your custom user model if you've defined one
            on_delete=models.CASCADE,
            related_name='userprofile',  # Specify the related name here
            null=True
        )

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




