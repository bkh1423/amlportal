from django.db import models


# ✅ 1. نوع النشاط التجاري (السؤال الأساسي الثابت)
class BusinessType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # مثل: Money Exchange, Insurance, BNPL

    def __str__(self):
        return self.name


# ✅ 2. السيناريو الرئيسي المرتبط بنوع النشاط
class Scenario(models.Model):
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE, related_name="scenarios")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.business_type.name} - {self.title}"


# ✅ 3. الأقسام الفرعية داخل السيناريو
class Section(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name="sections")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.scenario.title} - {self.name}"


# ✅ 4. الأسئلة داخل كل قسم
class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


# ✅ 5. الخيارات لكل سؤال (اختياري، مثل Yes / No)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


# ✅ 6. النتايج الخاصة بكل Business Type
class ScenarioResult(models.Model):
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE, related_name='results')
    title = models.CharField(max_length=255)
    
    # 🔸 الحقول الخاصة بالنتيجة
    output_type = models.CharField(max_length=100, default="Result")
    risk_level = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')
    recommended_services = models.TextField(blank=True, help_text="Example: AML Screening, eKYC, Transaction Monitoring")
    sanctions_list_activation = models.TextField(blank=True, help_text="Example: UNSC, OFAC, EU, SAMA")
    monitoring_frequency = models.CharField(max_length=100, blank=True, help_text="Example: Real-Time or Periodic")
    tags = models.TextField(blank=True, help_text="Example: High Risk, Geo-Flagged, Manual Review")
    
    # 🔸 الأكتفيت سيناريو / رولز الخاصة بكل نتيجة
    activated_scenarios = models.TextField(blank=True, help_text="List of activated rules or scenarios")

    # 🔸 الملخص النهائي للنتيجة
    output_summary = models.TextField(blank=True, help_text="Final summary or explanation of the result")

    def __str__(self):
        return f"{self.business_type.name} - {self.title} ({self.risk_level})"
