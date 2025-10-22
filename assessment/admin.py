from django.contrib import admin
from .models import BusinessType, Scenario, Section, Question, Choice, ScenarioResult


# ======== Inline Configurations ========
class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# ======== Admin Configurations ========

@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('title', 'business_type', 'is_active')
    list_filter = ('business_type', 'is_active')
    search_fields = ('title', 'business_type__name')
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'scenario')
    search_fields = ('name', 'scenario__title')
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'section')
    search_fields = ('text', 'section__name')
    inlines = [ChoiceInline]


@admin.register(ScenarioResult)
class ScenarioResultAdmin(admin.ModelAdmin):
    list_display = ('business_type', 'title', 'risk_level', 'monitoring_frequency')
    list_filter = ('business_type', 'risk_level')
    search_fields = ('title', 'business_type__name', 'tags')
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('business_type', 'title', 'output_type', 'risk_level')
        }),
        ('Details', {
            'fields': ('recommended_services', 'sanctions_list_activation', 'monitoring_frequency', 'tags')
        }),
        ('Activated Scenarios / Rules', {
            'fields': ('activated_scenarios',)
        }),
        ('Output Summary', {
            'fields': ('output_summary',)
        }),
    )
