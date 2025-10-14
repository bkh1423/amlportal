from django.db import models

class AssessmentResult(models.Model):
    """Stores final output and recommendations for each user"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    risk_level = models.CharField(max_length=50)
    recommended_services = models.TextField()
    monitoring_frequency = models.CharField(max_length=50)
    tags = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.user.username} ({self.risk_level})"
