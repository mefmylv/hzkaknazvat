from django.contrib import admin

from apps.users.models import Users

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'date_joined')
    list_filter = ('username', 'first_name', 'last_name', 'date_joined')