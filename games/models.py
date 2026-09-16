from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.BigIntegerField(default=100)

    def __str__(self):
        return f"{self.user.username} | {self.balance}"