from django.contrib import admin

# Register your models here.
from .models import Comment , Products

admin.site.register(Comment)
admin.site.register(Products)