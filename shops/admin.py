from django.contrib import admin
from shops.models import Shops


@admin.register(Shops)
class ShopsAdminView(admin.ModelAdmin):
    list_display = ('name', 'distance')
