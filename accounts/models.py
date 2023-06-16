from django.db import models


# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    national_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    # Additional fields for other user groups (researchers, hospitals, etc.) are be added here
