from django.contrib import admin
from .models import AssessmentResult

@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    # ✅ عرض نوع العمل بجانب مستوى الخطورة
    list_display = ('business_type', 'user', 'risk_level', 'monitoring_frequency', 'created_at')
    
    # ✅ إضافة فلترة حسب نوع العمل ومستوى الخطورة
    list_filter = ('business_type', 'risk_level')
    
    # ✅ تمكين البحث في نوع العمل ومستوى الخطورة
    search_fields = ('risk_level', 'business_type__name')
