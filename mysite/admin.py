from django.contrib import admin
from .models import Teaser

@admin.register(Teaser)
class TeaserAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
