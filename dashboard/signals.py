from django.db.models.signals import post_save
from django.dispatch import receiver
# from assessment.models import ScenarioResult   # ✅ مؤقتًا موقوف لأن الموديل غير موجود حاليًا
from .models import DashboardLog

# ✅ موقوف مؤقتًا لأننا حذفنا ScenarioResult من الموديلات
# @receiver(post_save, sender=ScenarioResult)
# def log_scenario_change(sender, instance, created, **kwargs):
#     """يسجل تلقائيًا كل تعديل أو إضافة في النتائج"""
#     if created:
#         action = f"تم إنشاء تقييم جديد: {instance.title}"
#     else:
#         action = f"تم تعديل تقييم: {instance.title}"

#     DashboardLog.objects.create(
#         action=action,
#         user_name="النظام",
#         details=f"مستوى الخطورة: {instance.risk_level} | نوع النشاط: {instance.business_type.name}"
#     )
