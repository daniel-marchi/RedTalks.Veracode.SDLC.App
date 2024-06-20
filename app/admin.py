from django.contrib import admin
from .models import User, Blab

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


@admin.register(Blab)
class BlabAdmin(admin.ModelAdmin):
    list_display = ['blabid', 'content', 'timestamp']

