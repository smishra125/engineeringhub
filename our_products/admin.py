from django.contrib import admin
from .models import OurProduct

@admin.register(OurProduct)
class OurProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_type', 'created_at')
    search_fields = ('title',)
    list_filter = ('product_type', 'created_at')