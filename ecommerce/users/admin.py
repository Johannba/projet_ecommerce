from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from ecommerce.users.models import Client


User = get_user_model()


admin.site.register(User, auth_admin.UserAdmin)
