from django.contrib import admin

from main.models import ChainLink


@admin.register(ChainLink)
class ChainAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "email", "country", "city", "product_name", "product_model",
        "exit_date",
        "provider", "debt", "company", "relationship_level")
    list_filter = ('city',)
