from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count
from assessment.models import BusinessType, Section 


def dashboard_home(request):
    """لوحة التحكم الرئيسية لعرض الإحصائيات"""

    # 👥 عدد المستخدمين
    users_count = User.objects.count()

    # 🧾 عدد التقييمات
    completed_evaluations = ScenarioResult.objects.count()

    # 📚 عدد الأقسام
    sections_count = Section.objects.count()

    # 📊 عدد التقييمات لكل نوع نشاط (Business Type)
    sections_data = (
        BusinessType.objects
        .annotate(result_count=Count('results'))
        .values('name', 'result_count')
    )

    # 🧩 توزيع التقييمات حسب مستوى الخطورة
    high_risk = ScenarioResult.objects.filter(risk_level='high').count()
    medium_risk = ScenarioResult.objects.filter(risk_level='medium').count()
    low_risk = ScenarioResult.objects.filter(risk_level='low').count()

    risk_values = [high_risk, medium_risk, low_risk]

    context = {
        'users_count': users_count,
        'completed_evaluations': completed_evaluations,
        'sections_count': sections_count,
        'sections_data': list(sections_data),
        'risk_values': risk_values,
    }

    return render(request, 'dashboard/home.html', context)


def contact_view(request):
    """صفحة التواصل"""
    return render(request, 'contact.html')
