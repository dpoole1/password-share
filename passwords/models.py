from django.db import models
from django.contrib.auth.models import User

# Holds secrets the users create
class Secret(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    destroy = models.BooleanField(default=True)