# models.py
from django.db import models

class Ariza(models.Model):
    ismi = models.CharField(max_length=100)
    email = models.EmailField()
    telefon_nomer = models.IntegerField(max_length=20, blank=True, null=True)
    xabar = models.TextField()

    def __str__(self):
        return self.ismi
