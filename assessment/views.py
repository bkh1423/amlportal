from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BusinessType, Section, Question, Choice, UserAnswer, ChoiceRule
from results.models import AssessmentResult


# 🟢 صفحة البداية
@login_required
def assessment_start(request):
    """صفحة البداية لبدء التقييم"""
    return render(request, 'assessment/assessment.html')


# 🟡 صفحة عرض الأقسام
@login_required
def assessment_sections(request):
    business_types = BusinessType.objects.all()
    if request.method == "POST":
        return redirect('assessment_select_type')
    return render(request, 'assessment/assessment_sections.html', {'business_types': business_types})


# 🟠 اختيار نوع النشاط التجاري
@login_required
def assessment_select_type(request):
    business_types = BusinessType.objects.all()

    if request.method == 'POST':
        selected_type = request.POST.get('business_type')
        if not selected_type:
            return render(request, 'assessment/select_type.html', {
                'business_types': business_types,
                'error': "Please select a business type."
            })

        business_type = get_object_or_404(BusinessType, id=selected_type)

        # ✅ نحفظ نوع النشاط في الـ session
        request.session['selected_business_type_id'] = business_type.id

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
            return redirect('calculate_result')

    return render(request, 'assessment/section_questions.html', {
        'business_type': business_type,
        'section': section,
        'questions': questions,
        'next_section': next_section,
    })


# ==============================================
# 🧠 حساب النتيجة الدقيقة حسب نوع العمل المختار
# ==============================================
@login_required
def calculate_result_view(request):
    """تحليل الإجابات وإظهار النتيجة الصحيحة حسب نوع العمل"""
    user = request.user
    user_answers = UserAnswer.objects.filter(user=user).select_related('choice', 'question__section')

    # ✅ إذا المستخدم ما جاوب على أي سؤال
    if not user_answers.exists():
        return render(request, 'results/no_result.html', {"message": "No answers found. Please complete the assessment first."})

    # ✅ نجيب نوع العمل من الـ session أو من أول إجابة (كحل احتياطي)
    business_type_id = request.session.get('selected_business_type_id')
    if business_type_id:
        business_type = get_object_or_404(BusinessType, id=business_type_id)
    else:
        business_type = user_answers.first().question.section.business_type

    # 🔹 جلب النتائج الخاصة بنفس نوع العمل فقط
    matched_results = []
    for answer in user_answers:
        rule = ChoiceRule.objects.filter(
            choice=answer.choice,
            scenario_result__business_type=business_type
        ).first()
        if rule:
            matched_results.append(rule.scenario_result)

    # ✅ لو ما فيه نتيجة مطابقة
    if not matched_results:
        return render(request, 'results/no_result.html', {"message": f"No result found for {business_type.name}."})

    # 🧩 اختيار أعلى مستوى خطورة
    priority = {"High": 3, "Medium": 2, "Low": 1}
    final_result = max(matched_results, key=lambda r: priority.get(r.risk_level, 0))

    # 🔸 نربط النتيجة بالنوع إذا مو مربوط
    if not final_result.business_type:
        final_result.business_type = business_type
        final_result.save()

    # 🎯 تحديد موقع المؤشر على الشريط
    if final_result.risk_level == "High":
        pointer_pos = "85%"
    elif final_result.risk_level == "Medium":
        pointer_pos = "50%"
    else:
        pointer_pos = "15%"

    # 🧹 نحذف session بعد الانتهاء
    request.session.pop('selected_business_type_id', None)

    # ✅ عرض صفحة النتيجة
    return render(request, 'assessment/scenario_result.html', {
        "result": final_result,
        "pointer_pos": pointer_pos,
        "business_type": business_type,
    })


# ==============================================
# 💡 صفحة الحلول (Solutions)
# ==============================================
@login_required
def solutions_page(request):
    """صفحة حلول FACEKI"""
    return render(request, 'solutions.html')
