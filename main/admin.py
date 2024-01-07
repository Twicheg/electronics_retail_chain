from django.contrib import admin

from main.models import ChainLink


@admin.register(ChainLink)
class ChainAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "email", "country", "city", "product_name", "product_model",
        "exit_date", "provider", "debt", "company", "relationship_level")
    list_filter = ('city',)
    actions = ["cancel_the_debt", ]
    change_form_template = "admin/my_change_form.html"

    @admin.action(description="cancel the debt")
    def cancel_the_debt(self, request, queryset):
        queryset.update(debt=0)

    def response_change(self, request, obj):
        if "cancel_the_debt" in request.POST:
            obj.debt = 0
            obj.save()
        return super().response_change(request, obj)
