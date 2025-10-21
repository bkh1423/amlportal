from django.contrib import admin
from .models import Scenario, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'scenario')

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')

admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(Question, QuestionAdmin)
