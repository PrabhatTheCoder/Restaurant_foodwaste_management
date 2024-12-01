from django.contrib import admin
from .models import RawMaterial

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'temperature', 'humidity', 'pH', 'microbial_count', 'weight', 
        'packaging_type', 'expired_at', 'is_wasted', 'client', 'created_at'
    )
    list_filter = ('packaging_type', 'is_wasted', 'client', 'created_at')
    search_fields = ('name', 'client__username')
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set client on creation
            obj.client = request.user
        super().save_model(request, obj, form, change)