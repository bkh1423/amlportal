from django.urls import path
from . import views

urlpatterns = [
    path('sections/', views.assessment_sections, name='assessment_sections'),
    path('start/', views.assessment_start, name='assessment_start'),  # ✅ تمت إضافته
    path('select-type/', views.assessment_select_type, name='assessment_select_type'),
    path('business/<int:business_type_id>/section/<int:section_id>/', views.section_questions_view, name='section_questions'),
    path('calculate-result/', views.calculate_result_view, name='calculate_result'),

]
