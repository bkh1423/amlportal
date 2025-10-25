from django.urls import path
from . import views

urlpatterns = [
    # صفحة الأقسام التعريفية (قبل البدء في التقييم)
    path('sections/', views.assessment_sections, name='assessment_sections'),

    # الصفحة الرئيسية للتقييمات (السيناريوهات)
    path('', views.scenarios_view, name='assessment_home'),

    # صفحة السيناريوهات المقسمة (Business / Compliance / Risk)
    path('scenarios/', views.scenarios_view, name='scenarios'),

    # صفحة عرض التفاصيل لكل سيناريو
    path('start/<int:scenario_id>/', views.start_scenario, name='start_scenario'),
]
