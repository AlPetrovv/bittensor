from django.contrib import admin
from django.contrib.admin import register

from ..models import Subnet


@register(Subnet)
class SubnetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "number")
    search_fields = ("name", "slug")
