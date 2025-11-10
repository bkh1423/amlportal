from django.shortcuts import render, get_object_or_404, redirect
from .models import BusinessType, Section, Question, Choice, UserAnswer
from django.contrib.auth.decorators import login_required
from results.models import AssessmentResult
from .models import ChoiceRule


# 🟢 صفحة البداية (Start Assessment)
@login_required
def assessment_start(request):
    """صفحة البداية فيها الزر Start Assessment"""
    return render(request, 'assessment/assessment.html')


# 🟡 صفحة عرض الأقسام + الزر Start في نفس الصفحة
@login_required
def assessment_sections(request):
    business_types = BusinessType.objects.all()

    if request.method == "POST":
        return redirect('assessment_select_type')

    return render(request, 'assessment/assessment_sections.html', {'business_types': business_types})


# 🟠 صفحة اختيار نوع العمل
@login_required
def assessment_select_type(request):
    business_types = BusinessType.objects.all()

    if request.method == 'POST':
        selected_type = request.POST.get('business_type')
        business_type = get_object_or_404(BusinessType, id=selected_type)
        first_section = Section.objects.filter(business_type=business_type).order_by('order').first()
        if first_section:
            return redirect('section_questions', business_type_id=business_type.id, section_id=first_section.id)

    return render(request, 'assessment/select_type.html', {'business_types': business_types})


# 🟣 عرض الأسئلة لكل قسم
@login_required
def section_questions_view(request, business_type_id, section_id):
    business_type = get_object_or_404(BusinessType, id=business_type_id)
    section = get_object_or_404(Section, id=section_id, business_type=business_type)
    questions = section.questions.prefetch_related('choices').all().order_by('id')

    next_section = Section.objects.filter(
        business_type=business_type,
        order__gt=section.order
    ).order_by('order').first()

    if request.method == "POST":
        for question in questions:
            choice_id = request.POST.get(f"q{question.id}")
            if choice_id:
                choice = Choice.objects.filter(id=choice_id).first()
                UserAnswer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'choice': choice}
                )

        if next_section:
            return redirect('section_questions', business_type_id=business_type.id, section_id=next_section.id)
        else:
            # ✅ الانتقال لصفحة النتيجة بعد آخر قسم
            return redirect('calculate_result')

    return render(request, 'assessment/section_questions.html', {
        'business_type': business_type,
        'section': section,
        'questions': questions,
        'next_section': next_section,
    })


# ==============================================
# 🧠 حساب النتيجة التلقائية من إجابات المستخدم
# ==============================================
@login_required
def calculate_result_view(request):
    """تحليل إجابات المستخدم وتحديد النتيجة الأنسب"""
    user = request.user
    user_answers = UserAnswer.objects.filter(user=user)

    matched_results = []

    for answer in user_answers:
        choice = answer.choice
        rule = ChoiceRule.objects.filter(choice=choice).first()
        if rule:
            matched_results.append(rule.scenario_result)

    if not matched_results:
        return render(request, 'results/no_result.html', {"message": "No matching result found."})

    # ✅ اختيار النتيجة الأعلى حسب مستوى الخطورة
    priority = {"High": 3, "Medium": 2, "Low": 1}
    final_result = max(matched_results, key=lambda r: priority.get(r.risk_level, 0))

    # ✅ عرض صفحة النتيجة الجاهزة
    return render(request, 'assessment/scenario_result.html', {"result": final_result})
