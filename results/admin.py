from django.contrib import admin
from .models import AssessmentResult

@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'risk_level', 'monitoring_frequency', 'created_at')
    list_filter = ('risk_level',)
