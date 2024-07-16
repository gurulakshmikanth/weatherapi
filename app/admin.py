from django.contrib import admin

# Register your models here.

from app.models import *

class ProfileAdminView(admin.ModelAdmin):
    list_display=['username']

admin.site.register(Profile,ProfileAdminView)

admin.site.register(weatherdata)