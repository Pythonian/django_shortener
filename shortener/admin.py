from django.contrib import admin
from .models import Shortener


@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    pass
