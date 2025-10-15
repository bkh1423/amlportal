from django.db import models

class UserProfile(models.Model):
    """Basic user profile linked to Django’s default User"""
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

