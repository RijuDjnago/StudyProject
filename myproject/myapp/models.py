from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", null=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="profile_image/", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"


