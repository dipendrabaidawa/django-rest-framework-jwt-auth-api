from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
import django.utils.timezone

class Candidate(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return self.title + ' ' + self.description + ' ' + self.published


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=200, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email