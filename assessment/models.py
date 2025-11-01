from django.db import models

# ✅ 1. نوع النشاط التجاري (Business Type)
class BusinessType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # مثل: Money Exchange, Insurance, BNPL

    def __str__(self):
        return self.name


# ✅ 2. الأقسام (Sections) المرتبطة بالنشاط التجاري
class Section(models.Model):
    business_type = models.ForeignKey(
        BusinessType,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="ترتيب القسم (1، 2، 3...)")  # ✅ ترتيب القسم

    class Meta:
        ordering = ['order']  # ✅ لعرض الأقسام بالترتيب الصحيح

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


# ✅ 5. النتائج الخاصة بكل Business Type
class ScenarioResult(models.Model):
    business_type = models.ForeignKey(
        BusinessType,
        on_delete=models.CASCADE,
        related_name='results'
    )
    title = models.CharField(max_length=255)
    output_type = models.CharField(max_length=100, default="Result")

    # 🔸 تفاصيل النتيجة
    risk_level = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')
    recommended_services = models.TextField(blank=True)
    sanctions_list_activation = models.TextField(blank=True)
    monitoring_frequency = models.CharField(max_length=100, blank=True)
    tags = models.TextField(blank=True)
    activated_scenarios = models.TextField(blank=True)
    output_summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.business_type.name} - {self.title} ({self.risk_level})"


# ✅ 6. حفظ إجابات المستخدم
class UserAnswer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:50]}"
