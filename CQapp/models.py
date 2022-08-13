from django.db import models

# Create your models here.
class Specialty(models.Model):
    name = models.CharField(max_length=50,blank=False)
    TYPE_CHOICES = (
        ('MANAGER', 'MANAGER'),
        ('CLIENT', 'CLIENT'),
    )
    type = models.CharField(max_length=254,choices=TYPE_CHOICES, default='MANAGER')

class CqUser(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=100)
    ROLE_CHOICES = (
        ('AUDITOR', 'AUDITOR'),
        ('MANAGER', 'MANAGER'),
        ('QA', 'QA'),
    )
    role = models.CharField(max_length=254,choices=ROLE_CHOICES)
    specialties = models.ManyToManyField(Specialty, related_name='user')

class CqTeam(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)
    members = models.ManyToManyField(CqUser, blank=True, related_name="members")






