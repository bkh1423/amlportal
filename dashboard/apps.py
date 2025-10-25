from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        # 🔔 استدعاء ملف الإشعارات (signals) لتفعيل الأحداث التلقائية
        import dashboard.signals
