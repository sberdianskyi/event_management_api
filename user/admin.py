from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    pass
