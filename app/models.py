"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Pledge(models.Model):
    email = models.EmailField()
    pledge = models.CharField(max_length=140)
    name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        default='Anonymous',
        help_text='Leave NAME blank to remain anonymous',
    )
    completed = models.BooleanField(default=False)
