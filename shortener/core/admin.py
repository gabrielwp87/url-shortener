from django.contrib import admin

from shortener.core.models import UrlRedirect


# Register your models here.

@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'created_in', 'updated_in')
