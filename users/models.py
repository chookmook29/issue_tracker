from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    contributions = models.IntegerField(default="0")
    amount_comments = models.IntegerField(default="0")
