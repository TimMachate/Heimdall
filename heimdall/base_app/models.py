from django.db import models

# Create your models here.
class navbar(models.Model):
    index1 = models.CharField(max_length=200)
    index2 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    index3 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )