from django.db import models

# السيناريو الرئيسي
class Scenario(models.Model):
    CATEGORY_CHOICES = [
        ('business', 'Business Profile'),
        ('compliance', 'Compliance Stack'),
        ('risk', 'Risk Evaluation'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# الأسئلة التابعة لكل سيناريو
class Question(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


# الخيارات لكل سؤال
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
