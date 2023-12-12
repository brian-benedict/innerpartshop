# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    model = UserProfile  # Use your custom user model
    list_display = ['username']  # Customize the displayed fields in the admin list

admin.site.register(UserProfile, CustomUserAdmin)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import UserProfile

# class CustomUserAdmin(UserAdmin):
#     model = UserProfile  # Update with your user model

# admin.site.register(UserProfile, CustomUserAdmin)