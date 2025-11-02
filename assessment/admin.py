from django.contrib import admin
from .models import BusinessType, Section, Question, Choice, UserAnswer


# ✅ Inline لعرض الخيارات داخل الأسئلة
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# ✅ Business Type
@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ✅ Section
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_type', 'order')
    list_editable = ('order',)
    list_filter = ('business_type',)
    search_fields = ('name', 'business_type__name')
    ordering = ('business_type', 'order')


# ✅ Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'section')
    list_filter = ('section',)
    search_fields = ('text', 'section__name')
    inlines = [ChoiceInline]


# ✅ User Answers
@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', 'submitted_at')
    list_filter = ('user', 'submitted_at')
