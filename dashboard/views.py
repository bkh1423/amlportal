from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Avg
from assessment.models import Section, ScenarioResult

def dashboard_home(request):
    """لوحة التحكم الرئيسية لعرض الإحصائيات"""

    # 👥 عدد المستخدمين
    users_count = User.objects.count()

    # 🧾 عدد التقييمات
    completed_evaluations = ScenarioResult.objects.count()

    # 📚 عدد الأقسام
    sections_count = Section.objects.count()

    # 📊 نسبة الامتثال لكل قسم
    sections_data = Section.objects.annotate(avg_score=Avg('scenarios__score')).values('name', 'avg_score')

    # 🧩 توزيع التقييمات حسب مستوى الخطورة
    high_risk = ScenarioResult.objects.filter(risk_level="High").count()
    medium_risk = ScenarioResult.objects.filter(risk_level="Medium").count()
    low_risk = ScenarioResult.objects.filter(risk_level="Low").count()

    # نحول القيم لقائمة JSON آمنة
    risk_values = [high_risk, medium_risk, low_risk]

    context = {
        'users_count': users_count,
        'completed_evaluations': completed_evaluations,
        'sections_count': sections_count,
        'sections_data': list(sections_data),
        'risk_values': risk_values,
    }

    return render(request, 'dashboard/home.html', context)
