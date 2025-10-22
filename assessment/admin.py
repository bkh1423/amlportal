from django.contrib import admin
from .models import Scenario, Section, Question, Choice, ScenarioResult


# 🔘 عرض الخيارات داخل السؤال
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# 📋 عرض الأسئلة داخل القسم
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# 📂 عرض الأقسام داخل السيناريو
class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


# ⚙️ لوحة السيناريو
@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    inlines = [SectionInline]
    search_fields = ('title',)
    list_filter = ('is_active',)


# ⚙️ لوحة الأقسام
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'scenario')
    inlines = [QuestionInline]
    list_filter = ('name', 'scenario')
    search_fields = ('scenario__title',)


# ⚙️ لوحة الأسئلة
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'section')
    inlines = [ChoiceInline]
    search_fields = ('text',)
    list_filter = ('section__scenario', 'section__name')


# ⚙️ لوحة النتائج النهائية
@admin.register(ScenarioResult)
class ScenarioResultAdmin(admin.ModelAdmin):
    list_display = ('scenario', 'risk_level', 'monitoring_frequency')
    search_fields = ('scenario__title', 'risk_level', 'tags')
    list_filter = ('risk_level', 'monitoring_frequency')
