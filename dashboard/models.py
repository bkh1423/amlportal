from django.db import models
from django.utils import timezone

class DashboardLog(models.Model):
    """
    نموذج بسيط لتسجيل العمليات أو الإحصائيات التي تظهر في لوحة التحكم
    """
    action = models.CharField(max_length=200, verbose_name="العملية")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاريخ الإنشاء")
    user_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="اسم المستخدم")
    details = models.TextField(blank=True, null=True, verbose_name="تفاصيل إضافية")

    def __str__(self):
        return f"{self.action} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        verbose_name = "سجل لوحة التحكم"
        verbose_name_plural = "سجلات لوحة التحكم"
        ordering = ['-created_at']
