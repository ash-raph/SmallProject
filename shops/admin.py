from django.contrib import admin
from shops.models import Shop


@admin.register(Shop)
class ShopsAdminView(admin.ModelAdmin):
    list_display = ('name', 'distance')
