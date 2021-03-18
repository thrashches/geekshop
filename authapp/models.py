from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(verbose_name="фото", upload_to="user_photo", blank=True)
    age = models.PositiveIntegerField(verbose_name="возраст", blank=True)

# Create your models here.
