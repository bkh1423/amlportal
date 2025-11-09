from django.db import models

class AssessmentResult(models.Model):
    """Stores final output and recommendations for each user"""
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None  # ✅ جعل الحقل اختياري مع قيمة افتراضية
    )
    
    # ✅ الحقل الجديد المطلوب
    business_type = models.ForeignKey(
        'assessment.BusinessType',
        on_delete=models.CASCADE,
        related_name='assessment_results',
        null=True, blank=True  # ✅ السماح بقيمة فارغة للبيانات القديمة
    )

    risk_level = models.CharField(max_length=50)
    recommended_services = models.TextField()
    monitoring_frequency = models.CharField(max_length=50)
    tags = models.TextField(blank=True, null=True)
    
    rules = models.TextField(blank=True, null=True, help_text="Enter rules or conditions linked to this result.")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.user.username if self.user else 'No User'} ({self.risk_level})"
