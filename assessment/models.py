from django.db import models

# 🧩 السيناريو الرئيسي (مثل Money Exchange / BNPL / Insurance)
class Scenario(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# 📂 الأقسام داخل السيناريو (Business Profile / Compliance Stack / Risk Evaluation)
class Section(models.Model):
    SECTION_CHOICES = [
        ('business', 'Business Profile'),
        ('compliance', 'Compliance Stack'),
        ('risk', 'Risk Evaluation'),
    ]

    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name="sections")
    name = models.CharField(max_length=20, choices=SECTION_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.scenario.title} - {self.get_name_display()}"


# ❓ الأسئلة داخل كل قسم
class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


# 🔘 الخيارات لكل سؤال
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


# 🧾 النتائج النهائية الخاصة بكل سيناريو
class ScenarioResult(models.Model):
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE, related_name="result")
    risk_level = models.CharField(max_length=50)
    recommended_services = models.TextField()
    sanctions_activation = models.TextField()
    monitoring_frequency = models.CharField(max_length=50)
    tags = models.TextField()
    output_summary = models.TextField()
    scenario_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.scenario.title} - {self.risk_level}"
