from django.contrib import admin
from .models import Assessment

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_type', 'customer_base_type', 'platform_type', 'created_at')
    list_filter = ('business_type', 'platform_type', 'location')
