from django.contrib import admin
from .models import FarmerData

@admin.register(FarmerData)
class FarmerDataAdmin(admin.ModelAdmin):
    list_display = ['farmer_name', 'crop_type', 'organic_type', 'village', 'district', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'crop_type', 'organic_type', 'water_source', 'district', 'state']
    search_fields = ['farmer_name', 'village', 'crop_type', 'farm_id', 'aadhaar_number']
    list_editable = ['is_approved']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Farmer Information', {
            'fields': ('user', 'farmer_name', 'phone_number', 'aadhaar_number', 'aadhaar_image')
        }),
        ('Farm Details', {
            'fields': ('farm_id', 'owner', 'land_area')
        }),
        ('Location Details', {
            'fields': ('village', 'district', 'state')
        }),
        ('Crop Information', {
            'fields': ('crop_type', 'organic_type')
        }),
        ('Agricultural Practices', {
            'fields': ('water_source', 'irrigation_type')
        }),
        ('Status & Timestamps', {
            'fields': ('is_approved', 'created_at', 'updated_at')
        }),
    )