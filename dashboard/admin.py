from django.contrib import admin
from .models import DashboardLog

@admin.register(DashboardLog)
class DashboardLogAdmin(admin.ModelAdmin):
    """عرض سجلات لوحة التحكم في صفحة الإدارة"""
    list_display = ('action', 'user_name', 'created_at')
    search_fields = ('action', 'user_name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

