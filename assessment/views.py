from django.shortcuts import render, get_object_or_404
from .models import ScenarioResult


def scenarios_view(request):
    """
    الصفحة الرئيسية للسيناريوهات (Scenarios)
    تعرض ثلاث مجموعات:
    - Business Profile
    - Compliance Stack
    - Risk Evaluation
    """
    business_scenarios = ScenarioResult.objects.filter(output_type__iexact='Business')
    compliance_scenarios = ScenarioResult.objects.filter(output_type__iexact='Compliance')
    risk_scenarios = ScenarioResult.objects.filter(output_type__iexact='Risk')

    context = {
        'business_scenarios': business_scenarios,
        'compliance_scenarios': compliance_scenarios,
        'risk_scenarios': risk_scenarios,
    }
    return render(request, 'assessment/scenarios.html', context)


def start_scenario(request, scenario_id):
    """
    صفحة عرض تفاصيل السيناريو المحدد عند الضغط على Start →
    """
    scenario = get_object_or_404(ScenarioResult, id=scenario_id)
    return render(request, 'assessment/start_scenario.html', {'scenario': scenario})
