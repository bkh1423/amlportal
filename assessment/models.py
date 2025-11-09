from django.db import models

# ✅ 1. نوع النشاط التجاري
class BusinessType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # مثل: Money Exchange, Insurance, BNPL

    def __str__(self):
        return self.name


# ✅ 2. الأقسام (Sections)
class Section(models.Model):
    business_type = models.ForeignKey(
        BusinessType,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="ترتيب القسم (1، 2، 3...)")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.business_type.name} - {self.name}"


# ✅ 3. الأسئلة داخل كل قسم
class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


# ✅ 4. الخيارات (Choices)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


# ✅ 5. حفظ إجابات المستخدم
class UserAnswer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:50]}"


# ✅ 6. جدول ربط الاختيارات بنتائج التقييم (ChoiceRule)
class ChoiceRule(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='rules')
    scenario_result = models.ForeignKey(
        'results.AssessmentResult',  # 🔹 تم التعديل هنا فقط
        on_delete=models.CASCADE,
        related_name='choice_rules'
    )
    condition_note = models.CharField(max_length=255, blank=True, null=True, help_text="سبب الربط (اختياري)")

    def __str__(self):
        return f"{self.choice.text} → {self.scenario_result}"
