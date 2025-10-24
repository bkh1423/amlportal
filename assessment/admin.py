from django.contrib import admin
from .models import BusinessType, Section, Question, Choice, ScenarioResult


# =======================
# Inline Configurations
# =======================

class ChoiceInline(admin.TabularInline):
    """لعرض الخيارات داخل صفحة السؤال"""
    model = Choice
    extra = 2


# =======================
# Admin Configurations
# =======================

@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    """إدارة نوع النشاط التجاري"""
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """إدارة الأقسام لكل نوع نشاط"""
    list_display = ('name', 'business_type')
    list_filter = ('business_type',)
    search_fields = ('name', 'business_type__name')
    # ✅ بدون Inline للأسئلة (الخيار الثاني اللي اخترتيه)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """إدارة الأسئلة لكل قسم"""
    list_display = ('text', 'section')
    list_filter = ('section',)
    search_fields = ('text', 'section__name')
    inlines = [ChoiceInline]


@admin.register(ScenarioResult)
class ScenarioResultAdmin(admin.ModelAdmin):
    """إدارة النتائج الخاصة بكل Business Type"""
    list_display = ('business_type', 'title', 'risk_level', 'monitoring_frequency')
    list_filter = ('business_type', 'risk_level')
    search_fields = ('title', 'business_type__name', 'tags')

    fieldsets = (
        ('Basic Info', {
            'fields': ('business_type', 'title', 'output_type', 'risk_level')
        }),
        ('Details', {
            'fields': (
                'recommended_services',
                'sanctions_list_activation',
                'monitoring_frequency',
                'tags'
            )
        }),
        ('Activated Scenarios / Rules', {
            'fields': ('activated_scenarios',)
        }),
        ('Output Summary', {
            'fields': ('output_summary',)
        }),
    )

