from django.contrib import admin

from shortener.core.models import UrlRedirect, UrlLog


# Register your models here.

@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'created_in', 'updated_in')


@admin.register(UrlLog)
class UrlLog(admin.ModelAdmin):
    list_display = ('origin', 'created_in', 'user_agent', 'host', 'ip', 'url_redirect')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

