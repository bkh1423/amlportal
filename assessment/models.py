from django.db import models

class Assessment(models.Model):
    """Stores user's assessment responses"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    business_type = models.CharField(max_length=100)
    customer_base_type = models.CharField(max_length=50)
    platform_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    compliance_team_size = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.business_type}"
