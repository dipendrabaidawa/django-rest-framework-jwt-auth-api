# from django.db import models
from djongo import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
import django.utils.timezone

class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    class Meta:
        abstract = True

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start = models.DateTimeField(default=django.utils.timezone.now(), verbose_name='date start')
    finish = models.DateTimeField(default=django.utils.timezone.now(), verbose_name='date end')
    location = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    is_experience_relevant = models.BooleanField(default=False)
    class Meta:
        abstract = True

class Education(models.Model):
    institution_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date start')
    finish = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date end')    
    class Meta:
        abstract = True

class Contact(models.Model):
    email = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    fb = models.CharField(max_length=200)
    class Meta:
        abstract = True

class Candidate(models.Model):
    full_name = models.CharField(max_length=70, default='SOME STRING')
    logo_url = models.CharField(max_length=200, default='SOME STRING')
    title = models.CharField(max_length=200, default='SOME STRING')
    location = models.CharField(max_length=200, default='SOME STRING')
    skills = models.ArrayField(model_container=Skill, default=[])
    exp = models.ArrayField(model_container=Experience, default=[])
    exp_total = models.IntegerField(default=0)
    exp_relevant_total = models.IntegerField(default=0)
    exp_last_total = models.IntegerField(default=0)
    educations = models.ArrayField(model_container=Education, default=[])
    contacts = models.EmbeddedField(model_container=Contact, default='')
    about = models.CharField(max_length=500, default='SOME STRING')

    def __str__(self):
        return self.full_name + " " + self.title


class CustomUser(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email